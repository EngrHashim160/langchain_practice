from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader('../source/cricket.txt')

docs = loader.load()


splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[4])