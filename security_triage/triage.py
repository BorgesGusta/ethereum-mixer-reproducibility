#!/usr/bin/env python3
"""Prototype: auditable human-in-the-loop triage of Ethereum model alerts.
No blockchain queries, no training, no automated blocking. Standard library only.
"""
import argparse
import datetime as dt
import hashlib
import json
import pathlib
import re

ADDR = re.compile(r'^0x[0-9a-fA-F]{40}$')
TX = re.compile(r'^0x[0-9a-fA-F]{64}$')
STATUSES = {'candidato', 'indeterminado', 'positivo_confirmado', 'negativo_confirmado', 'fora_do_escopo'}


def canonical(x):
    return json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def validate_case(item):
    if not isinstance(item, dict): raise ValueError('Case must be object')
    contract = item.get('contract', '')
    if not ADDR.fullmatch(contract): raise ValueError('Invalid contract address')
    score = item.get('model_score')
    if score is not None and (isinstance(score, bool) or not isinstance(score, (int, float)) or not 0 <= score <= 1):
        raise ValueError('model_score must be in [0,1] or null')
    evs = item.get('evidence', [])
    if not isinstance(evs, list): raise ValueError('evidence must be list')
    for ev in evs:
        if not isinstance(ev, dict): raise ValueError('evidence item must be object')
        if ev.get('type') not in ('tx_receipt', 'contract_source', 'protocol_docs', 'review_note'):
            raise ValueError('unsupported evidence type')
        if not isinstance(ev.get('source'), str) or not ev['source'].startswith(('https://', 'http://')):
            raise ValueError('evidence source URL required')
        if 'tx_hash' in ev and not TX.fullmatch(ev['tx_hash']): raise ValueError('invalid tx hash')
    return True


def triage(item):
    """Severity = evidence-completeness workflow, not illicitness or mixer probability."""
    validate_case(item)
    evs = item.get('evidence', [])
    kinds = {e['type'] for e in evs}
    supported_tx = any(e['type']=='tx_receipt' and e.get('receipt_ok') is True and
                       e.get('pool_log_verified') is True and TX.fullmatch(e.get('tx_hash', '')) for e in evs)
    result = {
        'contract': item['contract'].lower(), 'network': item.get('network', 'ethereum-mainnet'),
        'model_score': item.get('model_score'), 'evidence_count': len(evs),
        'receipt_and_log_supported': supported_tx,
        'status': 'indeterminado',
        'priority': 'revisar_evidencias' if supported_tx else 'coletar_evidencias',
        'reason_codes': (['TX_RECEIPT_POOL_LOG'] if supported_tx else ['NO_VERIFIED_POOL_RECEIPT']) +
                        (['SOURCE_DOCUMENTED'] if 'protocol_docs' in kinds or 'contract_source' in kinds else ['SOURCE_NOT_VERIFIED']),
        'action': 'REVIEW_ONLY', 'automated_blocking': False,
        'review_required': True,
        'caution': 'An observed withdrawal, a model score or a privacy tool alone does not establish illicit activity or mixer-class equivalence.'
    }
    return result


def append_audit(out_file, source, decisions):
    """Locally hash-linked JSONL; tamper-evident when anchor hash is independently kept."""
    out_file = pathlib.Path(out_file)
    if out_file.exists() and out_file.stat().st_size: raise FileExistsError('Refuse to overwrite existing audit log')
    prev = '0'*64
    with out_file.open('x', encoding='utf-8') as stream:
        for idx, dec in enumerate(decisions, 1):
            event = {'seq': idx, 'previous_hash': prev, 'source': source, 'decision': dec}
            h = hashlib.sha256(canonical(event).encode('utf-8')).hexdigest()
            event['event_hash'] = h
            stream.write(canonical(event) + '\n')
            prev = h
    return prev


def verify_audit(path):
    prev = '0'*64
    count = 0
    for line in pathlib.Path(path).read_text(encoding='utf-8').splitlines():
        entry = json.loads(line)
        expected = entry.pop('event_hash')
        if entry['previous_hash'] != prev or hashlib.sha256(canonical(entry).encode()).hexdigest() != expected:
            raise ValueError(f'Integrity failed at line {count+1}')
        prev = expected
        count += 1
    return {'events':count, 'last_hash':prev, 'valid':True}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('command', choices=('triage','verify'))
    p.add_argument('--input', required=True)
    p.add_argument('--output')
    args = p.parse_args()
    if args.command == 'verify':
        print(json.dumps(verify_audit(args.input), indent=2));return
    if not args.output: p.error('--output required for triage')
    raw = json.loads(pathlib.Path(args.input).read_text(encoding='utf-8'))
    if not isinstance(raw, list): raise ValueError('Input must be JSON array')
    results = [triage(e) for e in raw]
    last = append_audit(args.output, str(pathlib.Path(args.input).name), results)
    print(json.dumps({'cases':len(results), 'audit_log':args.output, 'last_hash':last, 'statuses':{'indeterminado':len(results)}}, ensure_ascii=False))

if __name__ == '__main__': main()
