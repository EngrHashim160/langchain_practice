from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader('../source/cricket.txt')

docs = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap=0,
)

doc_splits = splitter.split_documents(docs)

vector_store = Chroma(
    embedding_function=HuggingFaceEmbeddings(),
    persist_directory="my_chroma_db",
    collection_name="sample"
)

# add documents
vector_store.add_documents(doc_splits)

# view documents
# print(vector_store.get(include=['embeddings', 'documents', 'metadata']))

# printing just the top results
# print(
#     vector_store.similarity_search(
#         query="Some Legendary players in the cricket?",
#         k=1
#     )
# )

# printing top results with similarity score
print(
    vector_store.similarity_search_with_score(
        query="Some Legendary players in the cricket?",
        k=1
    )
)

# # meta-data filtering
# print(
#     vector_store.similarity_search_with_score(
#         query="",
#         filter={"source": ''} # not proper in my case here...
#     )
# )