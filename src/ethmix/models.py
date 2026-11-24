"""Classificador usado na reprodução consolidada.

As métricas por linha não demonstram generalização para novos contratos.
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.utils import resample
from .features import FEATURES

def novo_rf(seed=42):
    return RandomForestClassifier(
        n_estimators=100, max_depth=5, class_weight="balanced", random_state=seed
    )

def reamostrar(X: pd.DataFrame, y: pd.Series, seed=42):
    dados = X.copy().assign(_rotulo=np.asarray(y))
    negativos = dados[dados._rotulo == 0]
    positivos = dados[dados._rotulo == 1]
    if negativos.empty or positivos.empty:
        raise ValueError("Precisamos de observações das duas classes.")
    if len(positivos) < len(negativos):
        positivos = resample(positivos, replace=True,
                            n_samples=len(negativos), random_state=seed)
    equilibrado = pd.concat([negativos, positivos])
    return equilibrado[list(X.columns)], equilibrado["_rotulo"].astype(int)

def validar_cv(dados: pd.DataFrame, seed=42, n_splits=5):
    X = dados[list(FEATURES)]
    y = dados["label"].astype(int)
    if y.value_counts().min() < n_splits:
        raise ValueError("Há poucas observações para essa quantidade de divisões.")
    divisao = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed)
    registros = []
    for numero, (indices_treino, indices_teste) in enumerate(divisao.split(X, y), start=1):
        X_treino, y_treino = reamostrar(X.iloc[indices_treino], y.iloc[indices_treino], seed)
        modelo = novo_rf(seed)
        modelo.fit(X_treino, y_treino)
        previstos = modelo.predict(X.iloc[indices_teste])
        verdadeiros = y.iloc[indices_teste]
        registros.append({
            "fold": numero,
            "precision": precision_score(verdadeiros, previstos, zero_division=0),
            "recall": recall_score(verdadeiros, previstos, zero_division=0),
            "f1": f1_score(verdadeiros, previstos, zero_division=0),
        })
    return pd.DataFrame(registros)
