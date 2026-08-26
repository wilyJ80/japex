from transformers import pipeline
import pandas as pd

# Initialize the pipeline
pipe = pipeline("table-question-answering", model="google/tapas-base-finetuned-wtq")

# Load the CSV
df = pd.read_csv('src/table/licitacoes25-08-2026-16-44.csv')

# Convert all column values to strings to ensure Tapas compatibility
table = df.astype(str)

# Ask a question
query = "Qual é o objeto da licitação 054?"
result = pipe(table=table, query=query)
print(result)

