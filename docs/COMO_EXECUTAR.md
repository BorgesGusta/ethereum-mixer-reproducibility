# Como executar os notebooks

## Google Colab

1. No README, clique em **Abrir no Colab** no EXP01 ou EXP02.
2. Conecte o ambiente Python e execute as células de preparação e instalação.
3. Execute **Baixar e conferir os dados**. O notebook tenta baixar os dois arquivos processados publicados para leitura e valida seus hashes SHA-256.
4. Caso o Drive bloqueie o download automático, baixe os arquivos pelos links em `docs/DADOS.md` e envie-os pela janela do Colab.
5. Execute o experimento e confronte as saídas com `docs/RESULTADOS.md`.

Os dados brutos não são reconstruídos por esse procedimento. A execução completa com dados históricos ainda exige validação registrada em uma sessão limpa.

## No computador

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install notebook
PYTHONPATH=src python -m unittest discover -s tests -v
python -m notebook
```

Para EXP01/EXP02, os dois arquivos precisam estar na pasta `data/processed/` e passar na conferência de hashes.

Relatórios novos ficam em `results/generated/`, sem sobrescrever os históricos.
