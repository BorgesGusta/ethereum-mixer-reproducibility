# Dados para reproduzir os experimentos

Este repositório utiliza **dois arquivos processados** no EXP01 e no EXP02. Eles foram produzidos no projeto acadêmico original e não estão incluídos neste repositório.

## Arquivos necessários

| Arquivo | Uso | Tamanho registrado no Drive |
|---|---|---:|
| `features_treino.parquet` | Treino do classificador (123 janelas) | 13.025 bytes |
| `features_teste_20201029.parquet` | Avaliação do dia 29/10/2020 | 9.217.930 bytes |

### Verificação de integridade

Após carregar cada arquivo, o notebook calcula seu SHA-256 e compara com os valores do inventário original:

```text
features_treino.parquet
0a8baa11cee97d338d7a8d92b984f38192ba1a10ec915cc4a06d67ec94ad5c32

features_teste_20201029.parquet
6f8fd4e83e816c785d449116699065ad77425c9da6e7b19d9bcda36f42bddb51
```

Se o hash não corresponder, a execução é interrompida: o arquivo recebido não é idêntico à versão registrada.

## Origem e acesso aos arquivos

Os dois Parquets foram identificados na pasta `processed` do **Google Drive oficial da pesquisa**. **Os links diretos para download público ainda não foram incluídos**, porque, na conferência de permissões realizada em 23/11/2026, o Drive indicou acesso `anyone` com papel `writer` (edição) para os arquivos e a pasta. Antes de divulgar os links, é necessário revisar essas permissões e, se a equipe autorizar a distribuição, conceder somente leitura ao público.

Até essa revisão, quem tem acesso autorizado à pasta oficial deve baixar as cópias dos arquivos e fornecê-las manualmente ao Colab pela célula descrita abaixo. A pasta oficial do projeto é:

- [Projeto Mixers Ethereum — pasta da pesquisa](https://drive.google.com/drive/folders/1Dkz-82gKd7q3woGZDjEHl9IhQNnC7hgj)

Os arquivos Parquet são **dados processados**, não os dumps brutos. Reexecutar o notebook com eles não equivale a reconstruir as features diretamente dos registros da blockchain.

## Como carregar no Google Colab

1. Abra o EXP01 ou EXP02 usando o link no README.
2. Execute as células de preparação e instalação.
3. Na célula **Enviar e conferir os dados**, escolha os dois arquivos `.parquet` obtidos da fonte autorizada.
4. O notebook guarda os arquivos apenas na sessão temporária em `data/processed/`, verifica os hashes e interrompe caso haja divergência.
5. Execute as células seguintes e compare os resultados com `docs/RESULTADOS.md`.

O conteúdo carregado não é enviado ao GitHub. Sessões temporárias do Colab podem apagar arquivos ao serem encerradas.

## Para executar localmente

Coloque os arquivos em `data/processed/` na pasta do projeto e execute o notebook. A célula de carregamento reconhece os arquivos locais e verifica os hashes, sem solicitar novo upload.

## Demais experimentos

EXP03 a EXP10 dependem de artefatos específicos de análise e auditoria. Consulte cada notebook e `docs/CORRESPONDENCIA.md`. A existência de um link para o Colab não significa que o experimento esteja reproduzido ou que todos os insumos já sejam públicos.
