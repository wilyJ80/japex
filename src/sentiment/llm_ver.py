from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field, SecretStr

# INFO: o modelo local ignora a descricao!
# 1. Defina a estrutura de dados esperada usando Pydantic
class AnaliseSentimento(BaseModel):
    # O valor numérico estrito para o sentimento
    sentimento_id: int = Field(
        ..., 
        description="O número que define o sentimento: 1 para Positivo, 0 para Neutro, -1 para Negativo.",
        ge=-1,
        le=1
    )

# 2. Inicialize o cliente apontando para o seu servidor local do llama.cpp
# O llama.cpp simula a API da OpenAI, então usamos o ChatOpenAI mudando a base_url
llm = ChatOpenAI(
    base_url="http://localhost:8080/v1", # Ajuste a porta se o seu llama.cpp estiver em outra
    api_key=SecretStr("local-no-key"),               # O llama.cpp local não exige chave, mas o campo não pode ser nulo
    model="Qwen3.5-2B-Q8_0.gguf",            # Nome fictício ou o nome do seu modelo GGUF carregado
    temperature=0.0                       # Temperatura zero garante maior consistência no output estruturado
)

# 3. Vincule a estrutura do Pydantic ao modelo para forçar o output estruturado
llm_estruturado = llm.with_structured_output(AnaliseSentimento)

texts = [
    'Diferente das fotos do site. E ainda informou que não aceitaria a devolução porque estava com o lacre de frágil violado. Detalhe: eu recebi o produto com o lacre. Se eu não violasse ele, eu não conseguiria ver o produto. Fiz novo contato com o Mercado Livre e a inteligência artificial me disse que não havia mais recurso, que meu recurso tinha sido negado e que aquela era a última resposta. Surreal.',
    'Fiz a compra no dia 27.08 ate hoje nao recebi o pedido. Abri uma reclamacao tentaram me calar com um cupom de desconto de 30 reais que nao funciona e sobre a compra ate hoje nao foi entregue. Quero meu produto!',
    'E preciso com URGENCIA do dinheiro que está na conta pq meus compromissos estão vencendo e preciso paga-los como DINHEIRO que est bloqueado na conta do MERCADO PAGO E MERCADO LIVRE Isto é APROPRIÇÃO INDEBIRTA, que com urgência o desbloqueio da minha conta',
    'Fiz uma compra de um produto com envio FULL, e a data de entrega era para quarta feira, dia 19/08, porém, nessa data atualizaram que foram ao endereço e não puderam fazer entrega, o que é falso, pois o condomínio possui porteiro. Após esse dia, sempre atualizam que vão entregar no dia seguinte até as 21h e não sai para nova entrega, e só ficam postergando a data de entrega.',
    'Eu experimentei o produto dentro de casa, eu não saí com ele na rua. Se tivesse saído com ele, eu teria tirado a etiqueta',
    'NUNCA VI UMA EMPRESA NO BRASIL, RESOLVER UM PROBLEMA COM TANTA RAPIDEZ! PREFIRO COMPRAR NO MERCADO LIVRE DO QUE COMPRAR EM LOJA FÍSICA! MUITO MAIS RÁPIDO O ATENDIMENTO E MUITO MAIS EFICAZ!',
    'NUNCA VI UMA EMPRESA NO BRASIL, RESOLVER UM PROBLEMA COM TANTA RAPIDEZ! PREFIRO COMPRAR NO MERCADO LIVRE DO QUE COMPRAR EM LOJA FÍSICA!',
    'PREFIRO COMPRAR NO MERCADO LIVRE DO QUE COMPRAR EM LOJA FÍSICA!',
    'Muito boa e atendimento excelente'
]

for text in texts:
    resposta = llm_estruturado.invoke(
        f"Analise o sentimento do seguinte texto e retorne o ID correspondente, -1 negativo, 0 neutro, 1 positivo: {text}"
    )

    # 5. Acesse os dados diretamente como atributos do objeto
    print(f"ID do Sentimento: {resposta.sentimento_id}")
    print(resposta)

print("Expected: -1 -1 -1 0 0 1 1 0 1")
