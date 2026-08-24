import spacy
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pymupdf import pymupdf

# Load document

doc = pymupdf.open('./src/spacy_embeddings/Constituicao.pdf')
content = "".join(
    page.get_text('text')
    for page
        in pymupdf.open(doc)
)

assert content is not None
assert len(content) > 0
assert isinstance(content, str)

# Split document

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
splits = splitter.split_text(content)

assert splits is not None
assert len(splits) > 2
assert isinstance(splits, list)
assert all(isinstance(s, str) for s in splits)

# Embed

nlp = spacy.load('pt_core_news_lg')
docs = list(nlp.pipe(splits))
embeddings = [doc.vector for doc in docs]

# Search queries

search_queries = [
    nlp('Quais são as regras e os limites para o Estado cobrar tributos ou impostos?')
]

# Semantic search para cada query (Retornando os 3 maiores resultados no spaCy)
for query in search_queries:
    print(f"\n==================================================")
    print(f"Resultados para a pesquisa: '{query.text}'")
    print(f"==================================================")
    
    # Cria a lista com todos os scores e textos
    scores_e_textos = [
        (query.similarity(doc), split_texto) 
        for doc, split_texto in zip(docs, splits)
    ]
    
    # Ordena a lista do maior score para o menor
    scores_e_textos.sort(key=lambda x: x[0], reverse=True)
    
    # Pega apenas os 3 primeiros colocados
    top_3_resultados = scores_e_textos[:3]
    
    # Imprime os resultados formatados
    for ranking, (score, texto) in enumerate(top_3_resultados, start=1):
        print(f"\n[#{ranking}] Posição - Score: {score:.4f}")
        print(f"Trecho Correspondente:\n{texto}")
        print("-" * 50)
