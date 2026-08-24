from pydantic import SecretStr
import numpy as np
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from pymupdf import pymupdf

# 1. Load document
doc = pymupdf.open('./src/spacy_embeddings/Constituicao.pdf')
content = "".join(
    page.get_text('text')
    for page
        in pymupdf.open(doc)
)

assert content is not None
assert len(content) > 0
assert isinstance(content, str)

# 2. Split document
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
splits = splitter.split_text(content)

assert splits is not None
assert len(splits) > 2
assert isinstance(splits, list)
assert all(isinstance(s, str) for s in splits)

# 3. Inicializar Embeddings apontando para o servidor llama.cpp local
# O endpoint padrão do llama.cpp para compatibilidade com OpenAI é /v1
embeddings_model = OpenAIEmbeddings(
    base_url="http://localhost:8080/v1",
    api_key=SecretStr("local-llama-cpp-key"),  # Chave fictícia obrigatória
    model="embeddinggemma-300M-Q8_0.gguf"  # O modelo é definido pelo arquivo GGUF carregado no servidor
)

# Gerar embeddings para todos os chunks de texto
print("A gerar embeddings para o corpus (pode demorar alguns segundos)...")
corpus_embeddings = embeddings_model.embed_documents(splits[:4])

# 4. Search queries (Strings puras)
search_queries = [
    'Quais são as regras e os limites para o Estado cobrar tributos ou impostos?'
]

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# 5. Semantic search para cada query (Retornando os 3 maiores)
for query in search_queries:
    print(f"\n==================================================")
    print(f"Resultados para a pesquisa: '{query}'")
    print(f"==================================================")
    
    # Gerar vetor da query
    query_embedding = embeddings_model.embed_query(query)
    
    # Calcular a similaridade entre a query e cada split do documento
    scores_e_textos = [
        (cosine_similarity(query_embedding, doc_emb), split_texto) 
        for doc_emb, split_texto in zip(corpus_embeddings, splits)
    ]
    
    # Ordenar do maior score para o menor
    scores_e_textos.sort(key=lambda x: x[0], reverse=True)
    
    # Extrair os 3 primeiros colocados
    top_3_resultados = scores_e_textos[:3]
    
    # Imprimir no terminal
    for ranking, (score, texto) in enumerate(top_3_resultados, start=1):
        print(f"\n[#{ranking}] Posição - Score: {score:.4f}")
        print(f"Trecho Correspondente:\n{texto}")
        print("-" * 50)

