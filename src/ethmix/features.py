"""Cálculo dos atributos utilizado na reprodução.

Baseado no módulo versionado do projeto de pesquisa (17/11/2026).
Não muda a semântica dos campos da fonte nem substitui os dados auditados.
"""
import numpy as np
import pandas as pd

FEATURES = ("value_entropy", "fee_entropy", "internal_value_entropy", "call_count_mean")
DECIMAIS = {"value_eth": 4, "fee_eth": 6, "internal_value_eth": 4}

def preparar(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for coluna in ("value", "internal_value", "fee"):
        nome_eth = coluna + "_eth"
        if nome_eth not in df:
            if coluna not in df:
                raise KeyError(f"Coluna ausente: {coluna} ou {nome_eth}")
            df[nome_eth] = pd.to_numeric(df[coluna], errors="coerce") / 1e18
    df["time"] = pd.to_datetime(df["time"], utc=True)
    df["dia"] = df["time"].dt.date
    df["recipient"] = df["recipient"].astype(str).str.lower()
    df["call_count"] = pd.to_numeric(df["call_count"], errors="coerce")
    colunas = ["hash", "time", "dia", "sender", "recipient", "call_count",
               "value_eth", "internal_value_eth", "fee_eth"]
    return df[colunas]

def entropia(df: pd.DataFrame, chaves, coluna: str, decimais: int):
    chaves = list(chaves)
    valores = pd.to_numeric(df[coluna], errors="coerce").round(decimais)
    frequencias = df.assign(_valor=valores).groupby(
        chaves + ["_valor"], observed=True, dropna=False
    ).size()
    prob = frequencias / frequencias.groupby(level=chaves).transform("sum")
    return (-(prob * np.log2(prob))).groupby(level=chaves).sum()

def calcular_features(df: pd.DataFrame, chaves=("recipient", "dia")) -> pd.DataFrame:
    chaves = list(chaves)
    grupos = df.groupby(chaves, observed=True)
    resultados = pd.DataFrame({
        "n_tx": grupos.size(),
        "value_entropy": entropia(df, chaves, "value_eth", 4),
        "fee_entropy": entropia(df, chaves, "fee_eth", 6),
        "internal_value_entropy": entropia(df, chaves, "internal_value_eth", 4),
        "call_count_mean": grupos["call_count"].mean(),
    })
    return resultados.reset_index()
