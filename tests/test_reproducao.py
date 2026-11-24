import unittest
import numpy as np
import pandas as pd
from ethmix.features import preparar, calcular_features, FEATURES
from ethmix.models import novo_rf, reamostrar

class TestesReproducao(unittest.TestCase):
    def setUp(self):
        self.transacoes = pd.DataFrame({
            "hash": list("abcdef"),
            "time": ["2020-10-29T01:00:00Z"] * 6,
            "recipient": ["0xAb"] * 3 + ["0xCd"] * 3,
            "sender": ["0x1"] * 6,
            "call_count": [2, 4, 6, 10, 10, 10],
            "value_eth": [1., 1., 2., 3., 3., 3.],
            "fee_eth": [.01, .01, .02, .03, .03, .03],
            "internal_value_eth": [1., 1., 1., 2., 2., 2.]
        })

    def test_atributos(self):
        resultado = calcular_features(preparar(self.transacoes)).set_index("recipient")
        self.assertEqual(int(resultado.loc["0xab", "n_tx"]), 3)
        self.assertAlmostEqual(resultado.loc["0xab", "value_entropy"], 0.918295834, places=7)
        self.assertAlmostEqual(resultado.loc["0xab", "call_count_mean"], 4.)

    def test_balanceamento(self):
        X = pd.DataFrame({nome: np.arange(8, dtype=float) for nome in FEATURES})
        y = pd.Series([1] + [0] * 7)
        _, rotulos = reamostrar(X, y, seed=42)
        self.assertEqual(rotulos.value_counts().to_dict(), {0: 7, 1: 7})

    def test_modelo(self):
        modelo = novo_rf()
        self.assertEqual(modelo.n_estimators, 100)
        self.assertEqual(modelo.max_depth, 5)

if __name__ == "__main__":
    unittest.main()
