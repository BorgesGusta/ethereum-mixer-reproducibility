# Detecção de Mixers na Ethereum — Experimentos

Este repositório reúne os experimentos usados em uma pesquisa acadêmica sobre detecção de possíveis mixers na Ethereum. A ideia é facilitar a leitura e a repetição dos procedimentos em **Google Colab** ou em **Python local**, sem misturar versões históricas, dados brutos e resultados de execução.

Reproduzimos parte da abordagem apresentada por **Leale e Sendin (SBSeg 2025)**. Em 29/10/2020, a pesquisa original relatou 63 alertas e nossa reprodução registrou nove. Ambos recuperaram os três pools de referência, mas a diferença não foi totalmente explicada. **Um alerta não confirma que o contrato seja um mixer nem indica, por si só, atividade criminosa.**

## Executar no Google Colab

Abra o notebook desejado e execute as células na ordem.
Consulte os dados necessários antes de iniciar.

| Experimento | Descrição | Google Colab |
|---|---|---|
| EXP01 | Reprodução do artigo | [Abrir no Colab](https://colab.research.google.com/github/BorgesGusta/ethereum-mixer-reproducibility/blob/main/notebooks/EXP01-reproducao/EXP01.ipynb) |
| EXP02 | Sensibilidade dos filtros | [Abrir no Colab](https://colab.research.google.com/github/BorgesGusta/ethereum-mixer-reproducibility/blob/main/notebooks/EXP02-sensibilidade/EXP02.ipynb) |
| EXP03 | Alertas de 2020 | [Abrir no Colab](https://colab.research.google.com/github/BorgesGusta/ethereum-mixer-reproducibility/blob/main/notebooks/EXP03-alertas-2020/EXP03.ipynb) |
| EXP04 | Avaliação de 2026 | [Abrir no Colab](https://colab.research.google.com/github/BorgesGusta/ethereum-mixer-reproducibility/blob/main/notebooks/EXP04-avaliacao-2026/EXP04.ipynb) |
| EXP05 | Auditoria de contratos | [Abrir no Colab](https://colab.research.google.com/github/BorgesGusta/ethereum-mixer-reproducibility/blob/main/notebooks/EXP05-auditoria/EXP05.ipynb) |
| EXP06 | Controles e integridade | [Abrir no Colab](https://colab.research.google.com/github/BorgesGusta/ethereum-mixer-reproducibility/blob/main/notebooks/EXP06-controles-integridade/EXP06.ipynb) |
| EXP07 | Revisão humana | [Abrir no Colab](https://colab.research.google.com/github/BorgesGusta/ethereum-mixer-reproducibility/blob/main/notebooks/EXP07-revisao-humana/EXP07.ipynb) |
| EXP08 | Privacy Pools | [Abrir no Colab](https://colab.research.google.com/github/BorgesGusta/ethereum-mixer-reproducibility/blob/main/notebooks/EXP08-privacy-pools/EXP08.ipynb) |
| EXP09 | Classificadores | [Abrir no Colab](https://colab.research.google.com/github/BorgesGusta/ethereum-mixer-reproducibility/blob/main/notebooks/EXP09-classificadores/EXP09.ipynb) |
| EXP10 | Validação repetida | [Abrir no Colab](https://colab.research.google.com/github/BorgesGusta/ethereum-mixer-reproducibility/blob/main/notebooks/EXP10-validacao-repetida/EXP10.ipynb) |
| EXP11 | Triagem de segurança | [Abrir no Colab](https://colab.research.google.com/github/BorgesGusta/ethereum-mixer-reproducibility/blob/main/notebooks/EXP11-triagem/EXP11.ipynb) |

## Por onde começar?

1. Leia [os dados necessários](docs/DADOS.md). Os arquivos processados da pesquisa não são publicados automaticamente aqui.
2. Abra `notebooks/EXP01-reproducao/EXP01.ipynb` pelo GitHub/Colab ou execute no Jupyter local.
3. Execute as células na ordem. O notebook instala as dependências e indica onde colocar os arquivos necessários.
4. Compare a saída gerada com [os resultados registrados](docs/RESULTADOS.md).
5. Siga a ordem abaixo; os notebooks de auditoria funcionam com os artefatos próprios de cada etapa.

## Experimentos

| Notebook | Tema | Necessário para executar |
|---|---|---|
| EXP01 | Reprodução do artigo | Dados processados de treino e 2020 |
| EXP02 | Sensibilidade dos filtros | Mesmos dados do EXP01 |
| EXP03 | Alertas de 2020 | CSV de candidatos gerado no EXP01 |
| EXP04 | Avaliação de janeiro de 2026 | Dados processados de 2026 |
| EXP05 | Auditoria de transações | CSV de evidências amostradas |
| EXP06 | Controles e hashes | Arquivos e manifestos a conferir |
| EXP07 | Revisão humana | Duas fichas de classificação |
| EXP08 | Privacy Pools | Exportações de eventos históricos |
| EXP09 | Comparação de classificadores | Treino rotulado |
| EXP10 | Validação cruzada repetida | Treino rotulado |
| EXP11 | Triagem de segurança | Exemplo de entrada incluído |

Os nomes novos são mais simples; a [correspondência com os relatórios antigos](docs/CORRESPONDENCIA.md) mantém a rastreabilidade.

## Abrir no Colab

Entre no notebook desejado pelo GitHub e escolha **Open in Colab**, ou use `Arquivo → Abrir notebook → GitHub`. O código de inicialização busca este repositório público e instala as dependências. Para o EXP01, forneça os Parquets necessários conforme [docs/DADOS.md](docs/DADOS.md). Não é preciso dar acesso ao Google Drive da equipe.

## Rodar no computador

```bash
git clone https://github.com/BorgesGusta/ethereum-mixer-reproducibility.git
cd ethereum-mixer-reproducibility
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install notebook
python -m notebook
```

Para testar as funções: `PYTHONPATH=src python -m unittest discover -s tests -v`.

## Sobre os resultados

Todos os arquivos gerados devem ficar em `results/generated/`, ignorado pelo Git. As pontuações e métricas dos notebooks são exploratórias, salvo quando uma avaliação independente for documentada. Dados de treinamento positivos de um só contrato não permitem estimar generalização a contratos inéditos.

**Estado do pacote:** estrutura, código e testes locais preparados. A execução completa dos notebooks com os datasets históricos e a validação em uma sessão limpa do Colab ainda precisam ser conferidas. Leia os requisitos de cada notebook antes de usá-lo como evidência científica.
