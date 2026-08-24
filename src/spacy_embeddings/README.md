# Preparando o ambiente

- Baixe o modelo do spaCy: `uv run spacy download pt_core_news_lg`

- Suba o modelo de embeddings com o comando:

```
llama-server -m ./models/embeddinggemma-300M-Q8_0.gguf --embedding --pooling cls -b 1024 -ub 1024 -c 1024 -t 10
```

## Descrição

- Preparação, divisão de passagens e busca semântica de documentos.

## Protocolo de testes

- [x] Buscar base de dados

- [x] Automatizar a checagem do comportamento adequado do programa (testes de integração)

- [x] Documentar tempo e consumo de recursos total

- [x] Avaliar se resultados sustentam a tese

- [ ] Construir interface de texto para avaliação dos resultados

- [ ] Avaliar se modelo menor afeta resultados negativamente

## Resultados

- spaCy

    - Elapsed (wall clock) time (h:mm:ss or m:ss): 0:11.66

    - Maximum resident set size (kbytes): 1467784

    ```
    ==================================================
    Resultados para a pesquisa: 'Quais são as regras e os limites para o Estad
    o cobrar tributos ou impostos?'
    ==================================================

    [#1] Posição - Score: 0.7649
    Trecho Correspondente:
    IX - todos os julgamentos dos órgãos do Poder Judiciário serão públicos, e
     fundamentadas todas as decisões, sob
    pena de nulidade, podendo a lei, se o interesse público o exigir, limitar 
    a presença, em determinados atos, às próprias
    partes e a seus advogados, ou somente a estes;
    X - as decisões administrativas dos tribunais serão motivadas, sendo as di
    sciplinares tomadas pelo voto da maioria
    absoluta de seus membros;
    --------------------------------------------------

    [#2] Posição - Score: 0.7543
    Trecho Correspondente:
    § 1º Sempre que possível, os impostos terão caráter pessoal e serão gradua
    dos segundo a capacidade econômica
    do contribuinte, facultado à administração tributária, especialmente para 
    conferir efetividade a esses objetivos, identificar,
    respeitados os direitos individuais e nos termos da lei, o patrimônio, os 
    rendimentos e as atividades econômicas do
    contribuinte.
    § 2º As taxas não poderão ter base de cálculo própria de impostos.
    --------------------------------------------------

    [#3] Posição - Score: 0.7501
    Trecho Correspondente:
    respeitar todos os seus bens.    Regulamento
    § 1º São terras tradicionalmente ocupadas pelos índios as por eles habitad
    as em caráter permanente, as utilizadas
    para suas atividades produtivas, as imprescindíveis à preservação dos recu
    rsos ambientais necessários a seu bem-estar
    e as necessárias a sua reprodução física e cultural, segundo seus usos, co
    stumes e tradições.
    § 2º As terras tradicionalmente ocupadas pelos índios destinam-se a sua po
    sse permanente, cabendo-lhes o
    --------------------------------------------------
    ```

- embeddinggemma-300M-Q8_0.gguf

    - Elapsed (wall clock) time (h:mm:ss or m:ss): 0:03.19

    - Maximum resident set size (kbytes): 1045980

        - llama.cpp server

    ```
    ==================================================
    Resultados para a pesquisa: 'Quais são as regras e os limites para o Estad
    o cobrar tributos ou impostos?'
    ==================================================

    [#1] Posição - Score: 0.0438
    Trecho Correspondente:
    Presidência da República
    Casa Civil
    Subchefia para Assuntos Jurídicos
    CONSTITUIÇÃO DA REPÚBLICA FEDERATIVA DO BRASIL DE 1988
    Vide Emenda
    Constitucional nº 91, de
    2016
    Vide Emenda
    Constitucional nº 106,
    de 2020
    Vide Emenda
    Constitucional nº 107,
    de 2020
    (Vide Emenda
    Constitucional nº 132,
    de 2023)  Vigência
    (Vide Emenda
    Constitucional nº 132,
    de 2023)  Vigência
    Emendas Constitucionais
    Emendas Constitucionais de Revisão
    Ato das Disposições Constitucionais Transitórias
    --------------------------------------------------

    [#2] Posição - Score: 0.0141
    Trecho Correspondente:
    preconceitos, fundada na harmonia social e comprometida, na ordem interna 
    e internacional, com a solução pacífica das
    controvérsias, promulgamos, sob a proteção de Deus, a seguinte CONSTITUIÇÃ
    O DA REPÚBLICA FEDERATIVA DO
    BRASIL.
    TÍTULO I
    DOS PRINCÍPIOS FUNDAMENTAIS
      Art. 1º A República Federativa do Brasil, formada pela união indissolúv
    el dos Estados e Municípios e do
    Distrito Federal, constitui-se em Estado Democrático de Direito e tem como
     fundamentos:
    I - a soberania;
    II - a cidadania;
    --------------------------------------------------

    [#3] Posição - Score: -0.0609
    Trecho Correspondente:
    I - a soberania;
    II - a cidadania;
    III - a dignidade da pessoa humana;
    IV - os valores sociais do trabalho e da livre iniciativa;         (Vide L
    ei nº 13.874, de 2019)
    V - o pluralismo político.
    Parágrafo único. Todo o poder emana do povo, que o exerce por meio de repr
    esentantes eleitos ou diretamente,
    nos termos desta Constituição.
    21/08/26, 15:16
    Constituição
    https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm
    1/196
    --------------------------------------------------
    ```
