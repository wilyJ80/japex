from pydantic import SecretStr
from langchain_openai import ChatOpenAI
import pandas as pd
import numpy as np

# Load the CSV
df = pd.read_csv('src/table/licitacoes25-08-2026-16-44.csv')

df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16 = np.array_split(df, 16)

context = df1

model = ChatOpenAI(
    model="Qwen3VL-2B-Instruct-Q4_K_M.gguf",
    api_key=SecretStr('changeme'),
    base_url="https://dev.21t.com.br/v1",
    model_kwargs={
        "extra_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        }
    }
)

print(context)

response = model.invoke(
    f'''
    <sistema>
    Qual é o objeto da licitação 054?
    </sistema>
    <contexto>
    {context}
    </contexto>
    '''
)

print(response.content)
