from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='./source',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# Firstly using simple load
# docs = loader.load()

# Now, Using lazy_load()
docs = loader.lazy_load()

for document in docs:
    print(document.metadata)