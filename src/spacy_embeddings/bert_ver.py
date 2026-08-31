import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity

# 1. Carregar o modelo e o tokenizador
model_name = "Itau-Unibanco/NorBERTo-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# 2. Definir a consulta e a base de conhecimento
query = "Como posso redefinir a minha senha?"
documents = [
    "Esqueci a minha chave de acesso e preciso de ajuda.",
    "O horário de atendimento ao cliente é das 9h às 18h.",
    "Para atualizar o seu código secreto, clique em configurações de perfil.",
    "A entrega do produto costuma demorar até cinco dias úteis."
]

def get_embedding(text):
    # Tokenizar o texto de entrada
    inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    
    # Gerar os outputs do modelo sem calcular gradientes
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Utilizar a média dos embeddings da última camada oculta (Mean Pooling)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings.numpy()

# 3. Gerar embeddings para a query e para os documentos
query_embedding = get_embedding(query)
doc_embeddings = [get_embedding(doc) for doc in documents]

# 4. Calcular a similaridade e ordenar os resultados
print(f"Busca: '{query}'\n")
for doc, doc_emb in zip(documents, doc_embeddings):
    # Calcular a similaridade de cosseno
    similarity = cosine_similarity(query_embedding, doc_emb)[0][0]
    print(f"Score: {similarity:.4f} | Documento: {doc}")

