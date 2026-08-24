from medici import text
import spacy

nlp = spacy.load('pt_core_news_lg')

doc = nlp(text)

for ent in doc.ents:
    if ent.label_ == 'PER':
        print(f"Texto: {ent.text} | Categoria: {ent.label_} | Posição: {ent.start_char}")
