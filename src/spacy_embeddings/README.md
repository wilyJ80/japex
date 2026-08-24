# Preparando o ambiente

- Baixe o modelo do spaCy: `uv run spacy download pt_core_news_lg`

## Descrição

- Preparação, divisão de passagens e busca semântica de documentos.

## Protocolo de testes

- [x] Buscar base de dados

- [x] Automatizar a checagem do comportamento adequado do programa (testes de integração)

- [ ] Documentar tempo e consumo de recursos total

- [ ] Construir interface de texto para avaliação dos resultados

- [ ] Avaliar se resultados sustentam a tese

- [ ] Avaliar se modelo menor afeta resultados negativamente

## Resultados

- spaCy

    - Elapsed (wall clock) time (h:mm:ss or m:ss): 0:11.66

    - Maximum resident set size (kbytes): 1467784

- embeddinggemma-300M-Q8_0.gguf

    - Elapsed (wall clock) time (h:mm:ss or m:ss): 0:03.19

    - Maximum resident set size (kbytes): 1045980

    - `llama-server -m ./models/embeddinggemma-300M-Q8_0.gguf --embedding --pooling cls -b 1024 -ub 1024 -c 1024 -t 10`
