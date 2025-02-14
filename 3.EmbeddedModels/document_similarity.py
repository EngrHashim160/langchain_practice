from langchain_huggingface import HuggingFaceEmbeddings
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
load_dotenv()

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Babar Azam is a Pakistani cricketer known for his elegant batting and consistency.",
    "Shaheen Afridi is a Pakistani fast bowler known for his lethal pace and swing.",
    "Mohammad Rizwan is a wicketkeeper-batsman famous for his resilience and adaptability.",
    "Shadab Khan is an all-rounder known for his sharp leg-spin and aggressive batting.",
    "Fakhar Zaman is known for his explosive batting and his historic double century in ODIs."
]

query = "tell me about Fakhar Zaman"

doc_embeddings = embedding.embed_documents(documents)

query_embeddings = embedding.embed_query(query)

scores = cosine_similarity([query_embeddings], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print(f"Similarity Score is {score}")