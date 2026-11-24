# Dados necessários

Os arquivos brutos **não** são fornecidos neste repositório. O pacote foi preparado para que não seja preciso acessar uma pasta privada de outro pesquisador, mas quem executar a reprodução completa precisará obter os dados legalmente e conferir sua procedência.

## EXP01 e EXP02

Coloque estes arquivos em `data/processed/`:

- `features_treino.parquet`: 123 observações rotuladas do treino legado. Colunas: `label`, `n_tx` e quatro atributos.
- `features_teste_20201029.parquet`: atributos dos destinatários em 29/10/2020. Colunas: `recipient`, `n_tx`, `tornado` e quatro atributos.

SHA-256 registrados em relatório anterior:

- Treino: `0a8baa11cee97d338d7a8d92b984f38192ba1a10ec915cc4a06d67ec94ad5c32`
- 2020: `6f8fd4e83e816c785d449116699065ad77425c9da6e7b19d9bcda36f42bddb51`

Esses hashes verificam se os arquivos correspondem **àqueles do registro histórico**, não sua qualidade científica. Para executar a partir de dumps brutos, será necessária uma etapa adicional de extração e padronização que ainda não está disponível aqui como execução pública validada.

## Demais experimentos

Algumas etapas usam relatórios ou amostras de auditoria. Os notebooks indicam o formato esperado. Não há necessidade de publicar endereços privados, credenciais, tokens nem dados de terceiros sem autorização.

Se você fizer upload manual no Colab, descompacte ou mova os arquivos para a pasta `data/processed/` do clone temporário. O código não faz acesso automático ao Drive da equipe.
