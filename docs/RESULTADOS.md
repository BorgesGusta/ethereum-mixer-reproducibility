# Resultados de referência (não recalculados nesta publicação)

A tabela registra números presentes nos relatórios do projeto original, não resultados produzidos automaticamente pelos notebooks deste repositório.

| Experimento | Resultado registrado | Limitação |
|---|---|---|
| EXP01 | 9 alertas em 29/10/2020, 3/3 pools de referência | Estudo original relata 63; paridade parcial |
| EXP02 | 49, 14, 9 e 7 alertas para mínimo de 1, 5, 10 e 20 transações | Não mede precisão nem falsos positivos |
| EXP04 | 9 alertas em 15/01/2026 com limiar 0,85 | 6 candidatos sem rótulo independente |
| EXP05 | 18/18 transações amostradas conferidas; 586 logs das 18 | Amostra não representa todas as transações |
| EXP07 | 4 discordâncias entre duas fichas com apoio de IA | Sem revisão cega independente nem homologação |
| EXP08 | 4 retiradas históricas de sucesso examinadas | Não prova equivalência funcional a Tornado Cash |
| EXP09 | RF: F1 médio interno de 0,9778 no EXP-07 original | Positivos vêm de um único contrato |
| EXP10 | Extra Trees: F1 0,9810 ± 0,0018 | Validação interna por observação |
| EXP11 | Protótipo offline; quatro testes registrados | Não verifica blockchain nem bloqueia operações |

Os procedimentos reconstruídos no pacote público devem ser comparados aos registros originais antes de declarar reprodução confirmada.
