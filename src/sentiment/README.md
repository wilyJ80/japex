# Preparando o ambiente

```
llama-server -m ./models/Qwen3.5-2B-Q8_0.gguf -c 1024 -b 1024 -ub 1024 -t 10 --reasoning off
```

## Descrição

- Análise de sentimento de textos com LLMs e NLTK.

## Protocolo de testes

- [x] Buscar base de dados

- [ ] ~Automatizar a checagem do comportamento adequado do programa (testes de integração)~

- [ ] Documentar tempo e consumo de recursos total

- [ ] Avaliar se resultados sustentam a tese

- [ ] Construir interface de texto para avaliação dos resultados

- [ ] Avaliar se modelo menor afeta resultados negativamente

## Resultados

- NLTK (leia-br)

    - Elapsed (wall clock) time (h:mm:ss or m:ss): 0:00.07

    - Maximum resident set size (kbytes): 40016

- LLM (qwen 2b)

    - Elapsed (wall clock) time (h:mm:ss or m:ss): 0:35.57

    - Maximum resident set size (kbytes): 2534052
