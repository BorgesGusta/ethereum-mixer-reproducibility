# Guia rápido

## Google Colab

1. Entre em `https://colab.research.google.com/` e escolha `GitHub`.
2. Abra o repositório `BorgesGusta/ethereum-mixer-reproducibility` e selecione o notebook desejado.
3. Execute a primeira célula. Ela utiliza o código publicado neste repositório.
4. Para EXP01/EXP02, coloque os Parquets autorizados em `data/processed/` dentro da sessão Colab. A pasta local do Colab é temporária.
5. Execute as demais células. Consulte `docs/RESULTADOS.md` para comparação.

## Python local

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install notebook
PYTHONPATH=src python -m unittest discover -s tests -v
python -m notebook
```

As figuras, logs e tabelas novas devem ser salvos em `results/generated/` e não substituem resultados históricos.
