# Alternativas a LLMs

## Preparando o ambiente

- Instale o `uv`

- Sincronize o ambiente com `uv sync`

- Instale o projeto com `uv pip install -e .`

- Siga as instruções na pasta de cada experimento.

## O que consta no documento:

- [x] spaCy vs embeddings locais

    - Destacar arquitetura `word2vec`

- [ ] MobileNet (mediapipe) vs embeddings CLIP (transformers) para embeddings multimodais

- [ ] PaddleOCR

- [ ] spaCy NER vs GliNER/LLM

- [ ] Busca semantica vs BM25: exemplo ChatUNEB

## Outras possibilidades

- [ ] Analise de Sentimento: NLTK pacote `leia-br`

- [ ] Analise de palavras mais comuns: spaCy (lemmatizer) e NLTK (senter)

- [ ] YOLOv26 classifier

## Metodologia

- Dois scripts para cada experimento (LLMs/transformers vs alternativas), comparação de tempo de execução e consumo de recursos, ambos medidos com o comando `/usr/bin/time -v`.

    - Output melhor? Como fazer?

## Limitações

- Grande progresso no desempenho de LLMs locais, mas soluções alternativas, por exemplo baseadas em redes neurais, ainda são muito escassas.

    - Exemplo: Mamba/RWKV para geração de texto e reranking
