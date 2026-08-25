# Preparando o ambiente

```
llama-server -m ./models/Qwen3.5-2B-Q8_0.gguf -c 1024 -b 1024 -ub 1024 -t 10 --reasoning off
```

## Descrição

- Análise de sentimento de textos com LLMs e NLTK.

## Protocolo de testes

- [x] Buscar base de dados

- [ ] ~Automatizar a checagem do comportamento adequado do programa (testes de integração)~

- [x] Documentar tempo e consumo de recursos total

- [ ] Avaliar se resultados sustentam a tese

- [ ] Construir interface de texto para avaliação dos resultados

- [ ] Avaliar se modelo menor afeta resultados negativamente

## Resultados

- NLTK (leia-br)

    - Elapsed (wall clock) time (h:mm:ss or m:ss): 0:00.07

    - Maximum resident set size (kbytes): 42016

    - Percent of CPU this job got: 64%

    - CPU: 64 * 0.07 = 4,48

    - Taxa de acerto: 6/9

- Modelo BERT

    - Elapsed (wall clock) time (h:mm:ss or m:ss): 0:04.96

    - Maximum resident set size (kbytes): 1073748

    - Percent of CPU this job got: 135%

    - CPU: 135 * 5 = 675

    - Taxa de acerto: 8/9

- LLM (qwen 2b Q8_0): ```llama-server -m ./models/Qwen3.5-2B-Q8_0.gguf -c 1024 -b 1024 -ub 1024 -t 10 --reasoning off```

    - Elapsed (wall clock) time (h:mm:ss or m:ss): 0:35.57

    - Maximum resident set size (kbytes): 2534052

    - Percent of CPU this job got: 669%

    - CPU: 669 * 35.57 =  23796,33

    - Taxa de acerto: 5/9

### Conclusões

- Diferença grande de cada um dos métodos: em duas ordens de grandeza!
