"""Leitura de dados e execução com saídas salvas localmente."""
from pathlib import Path
import hashlib
import json
import joblib
import pandas as pd
from .features import FEATURES
from .models import novo_rf, reamostrar, validar_cv

HASHES_REFERENCIA = {
    "features_treino.parquet": "0a8baa11cee97d338d7a8d92b984f38192ba1a10ec915cc4a06d67ec94ad5c32",
    "features_teste_20201029.parquet": "6f8fd4e83e816c785d449116699065ad77425c9da6e7b19d9bcda36f42bddb51",
}

def abrir_dados(caminho, obrigatorias):
    caminho = Path(caminho)
    if not caminho.exists():
        raise FileNotFoundError(
            f"Arquivo ausente: {caminho}. Leia docs/DADOS.md antes de executar."
        )
    if caminho.suffix == ".parquet":
        df = pd.read_parquet(caminho)
    elif caminho.suffix == ".csv":
        df = pd.read_csv(caminho)
    else:
        raise ValueError("Use arquivo CSV ou Parquet.")
    faltam = sorted(set(obrigatorias) - set(df.columns))
    if faltam:
        raise ValueError(f"Colunas ausentes em {caminho.name}: {faltam}")
    return df

def sha256(caminho):
    h = hashlib.sha256()
    with open(caminho, "rb") as arquivo:
        for trecho in iter(lambda: arquivo.read(1024 * 1024), b""):
            h.update(trecho)
    return h.hexdigest()

def verificar_referencia(caminho):
    caminho = Path(caminho)
    esperado = HASHES_REFERENCIA.get(caminho.name)
    calculado = sha256(caminho)
    return {"arquivo": caminho.name, "sha256": calculado,
            "hash_referencia": esperado,
            "igual_referencia": None if esperado is None else calculado == esperado}

def treinar(treino, seed=42, min_tx=10):
    elegiveis = treino.loc[treino["n_tx"] >= min_tx].copy()
    cv = validar_cv(elegiveis, seed=seed)
    X, y = reamostrar(elegiveis[list(FEATURES)], elegiveis["label"].astype(int), seed)
    modelo = novo_rf(seed)
    modelo.fit(X, y)
    return modelo, cv

def prever(modelo, teste, min_tx=10, limiar=0.50):
    elegiveis = teste.loc[teste["n_tx"] >= min_tx].copy()
    elegiveis["score"] = modelo.predict_proba(elegiveis[list(FEATURES)])[:, 1]
    elegiveis["alerta"] = elegiveis["score"] > limiar
    return elegiveis

def guardar_arquivos(pasta, modelo, cv, alertas, manifesto):
    pasta = Path(pasta)
    pasta.mkdir(parents=True, exist_ok=True)
    cv.to_csv(pasta / "validacao.csv", index=False)
    alertas.to_csv(pasta / "alertas.csv", index=False)
    joblib.dump(modelo, pasta / "modelo_rf.joblib")
    (pasta / "manifesto.json").write_text(
        json.dumps(manifesto, ensure_ascii=False, indent=2), encoding="utf-8"
    )
