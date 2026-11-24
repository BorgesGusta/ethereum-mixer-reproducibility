import json
import pathlib
import tempfile
import unittest
from triage import triage, append_audit, verify_audit

ROOT = pathlib.Path(__file__).parent

class Tests(unittest.TestCase):
    def setUp(self): self.data=json.loads((ROOT/'sample_cases.json').read_text())
    def test_full_evidence_does_not_auto_label(self):
        d=triage(self.data[0]);self.assertEqual(d['status'],'indeterminado');self.assertEqual(d['priority'],'revisar_evidencias');self.assertFalse(d['automated_blocking'])
    def test_high_score_without_evidence_does_not_auto_block(self):
        d=triage(self.data[1]);self.assertEqual(d['priority'],'coletar_evidencias');self.assertFalse(d['automated_blocking'])
    def test_invalid_address(self):
        d=dict(self.data[0]);d['contract']='bad';self.assertRaises(ValueError,triage,d)
    def test_integrity_tamper(self):
        with tempfile.TemporaryDirectory() as td:
            out=pathlib.Path(td)/'audit.jsonl'
            append_audit(out,'fixture.json',[triage(e) for e in self.data]);self.assertTrue(verify_audit(out)['valid'])
            raw=out.read_text();out.write_text(raw.replace('REVIEW_ONLY','AUTO_BLOCK',1));self.assertRaises(ValueError,verify_audit,out)

if __name__=='__main__': unittest.main()
