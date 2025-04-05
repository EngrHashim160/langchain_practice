from langchain_community.document_loaders import CSVLoader

loader = CSVLoader('./source/sample.csv')

docs = loader.load()

print(len(docs))
print(docs[10].page_content)