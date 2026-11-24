# Como executar os notebooks

## Google Colab

1. No README, clique em **Abrir no Colab** no experimento desejado.
2. Conecte o ambiente Python.
3. Execute as células de preparação e instalação na ordem.
4. Para EXP01 e EXP02, obtenha os dois Parquets por meio de acesso autorizado à pasta oficial da pesquisa, conforme `docs/DADOS.md`.
5. Execute a célula **Enviar e conferir os dados**. Ela aceita upload manual, verifica nome e SHA-256 e armazena os arquivos apenas na sessão temporária.
6. Execute o experimento e confronte a saída com `docs/RESULTADOS.md`.

**Importante:** os arquivos ainda não estão disponíveis para download público automatizado. Não altere as permissões de compartilhamento sem revisão da equipe. As etapas com dados reais ainda precisam de uma execução completa documentada no Colab.

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
