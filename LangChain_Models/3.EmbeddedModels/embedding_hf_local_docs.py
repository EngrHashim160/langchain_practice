from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

documents = [
    'Islamabad is the Capital of Pakistan.',
    'Delhi is the capital of India',
    'Paris is the capital of France'
]

vector = embedding.embed_documents(documents)

print(vector)