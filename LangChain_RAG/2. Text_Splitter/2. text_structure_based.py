from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader('../source/cricket.txt')

docs = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap=0,
)

print(docs[0].page_content)

result = splitter.split_documents(docs)

print(result)