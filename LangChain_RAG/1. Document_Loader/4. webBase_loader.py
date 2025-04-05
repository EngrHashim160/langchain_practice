from langchain_community.document_loaders import WebBaseLoader

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv() 

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text - \n {text}",
    input_variables=['question', 'text']
)


model = ChatGroq(model="deepseek-r1-distill-qwen-32b")

parser = StrOutputParser()

url = 'https://www.grammarly.com/blog/parts-of-speech/articles/'
loader = WebBaseLoader(url) # we can use list of variables

docs = loader.load()

chain = prompt | model | parser

result = chain.invoke({
    'question': 'What Are Articles in English Grammar?',
    'text' : docs[0].page_content
})

print(result)