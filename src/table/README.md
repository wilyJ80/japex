# Preparando o ambiente

- Suba o modelo de LLM com o comando:

```
```

## Descrição

- Leitura de planilhas.

## Protocolo de testes

- [x] Buscar base de dados

- [x] Documentar tempo e consumo de recursos total

- [x] Avaliar se resultados sustentam a tese

- [ ] Construir interface de texto para avaliação dos resultados

- [ ] Avaliar se modelo menor afeta resultados negativamente

## Limitações

- Para executar os testes em tempo hábil, foi selecionada uma tabela de tamanho reduzido, para poder rodar uma LLM com uma janela de contexto menor a fim de reduzir latência a níveis possíveis de se trabalhar.

## Resultados

- BERT

    - Elapsed (wall clock) time (h:mm:ss or m:ss): 0:10.49
    
    - Percent of CPU this job got: 101%

    - Maximum resident set size (kbytes): 1270448

    - ```
        {'answer': 'Contratação de empresa especializada em construção civil para execução de pavimentação em bloquetes sextavados de concreto nas Ruas João Alves Motoso e São João, no Distrito de Ijicatu, com área aproximada de 3.104,67 m², no Município de José Gonçalves de Minas/MG., Contratação de empresa  especializada para execução de obra de engenharia destinada à revitalização de canteiros  centrais e urbanização de vias, incluindo pavimentação, drenagem superficial, meios-fios,  sarjetas, paisagismo, iluminação pública e demais serviços previstos nos projetos  técnicos e documentos queintegram o processo administrativo, na Comunidade de  Catutiba, Município de José Gonçalves de Minas/MG', 'coordinates': [(0, 3), (2, 3)], 'cells': ['Contratação de empresa especializada em construção civil para execução de pavimentação em bloquetes sextavados de concreto nas Ruas João Alves Motoso e São João, no Distrito de Ijicatu, com área aproximada de 3.104,67 m², no Município de José Gonçalves de Minas/MG.', 'Contratação de empresa especializada para execução de obra de engenharia destinada à revitalização de canteiros  centrais e urbanização de vias, incluindo pavimentação, drenagem superficial, meios-fios,  sarjetas, paisagismo, iluminação pública e demais serviços previstos nos projetos  técnicos e documentos que integram o processo administrativo, na Comunidade de  Catutiba, Município de José Gonçalves de Minas/MG'], 'aggregator': 'NONE'}
    ```

- LLM

    - Elapsed (wall clock) time (h:mm:ss or m:ss): 0:21.64

    - ```
        > **Contratação de empresa especializada para execução de obra de engenhar
        ia destinada à revitalização de canteiros centrais e urbanização de vias, 
        incluindo pavimentação, drenagem superficial, meios-fios, sarjetas, paisag
        ismo, iluminação pública e demais serviços previstos nos projetos técnicos
         e documentos que integram o processo administrativo, na Comunidade de Cat
        utiba, Município de José Gonçalves de Minas/MG.**
    ```
