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

Os dois arquivos processados estão disponíveis para leitura no Google Drive da pesquisa:

- [Baixar features_treino.parquet](https://drive.google.com/file/d/1jUHAq6H9FKSgptv4nsCoOmFILH4Py_2S/view)
- [Baixar features_teste_20201029.parquet](https://drive.google.com/file/d/1g22eCccxC4v_S2RmxPhFZyzfF1ARuzPk/view)

[Pasta dos dados processados](https://drive.google.com/drive/folders/18IeCuFcx5ka0OoJAxjJt3gey7JVX71ht)

A permissão de leitura pública foi conferida em 23/11/2026.

Esses arquivos contêm dados processados. Seu uso não equivale à reconstrução completa das características a partir dos registros brutos da blockchain.

## Como carregar no Google Colab

1. Abra o EXP01 ou EXP02 pelo botão do README e conecte a sessão.
2. Execute as células de preparação e instalação.
3. Execute **Baixar e conferir os dados**. A célula tenta obter os dois Parquets dos links públicos do Google Drive e verifica os hashes SHA-256 registrados acima.
4. Se o Drive negar o download automático, use a janela de envio manual exibida pelo Colab e escolha os arquivos baixados pelos links acima.
5. Execute as demais células e compare as saídas com `docs/RESULTADOS.md`.

O código não utiliza credenciais do Google Drive e não envia os arquivos ao GitHub. Eles ficam apenas na sessão temporária do Colab.

## Para executar localmente

Coloque os arquivos em `data/processed/` na pasta do projeto e execute o notebook. A célula de carregamento reconhece os arquivos locais e verifica os hashes, sem solicitar novo upload.

## Demais experimentos

EXP03 a EXP10 dependem de artefatos específicos de análise e auditoria. Consulte cada notebook e `docs/CORRESPONDENCIA.md`. A existência de um link para o Colab não significa que o experimento esteja reproduzido ou que todos os insumos já sejam públicos.
