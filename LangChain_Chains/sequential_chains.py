from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

model = ChatGroq(model="mixtral-8x7b-32768")

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({'topic': 'Gen AI'})

print(response)

chain.get_graph().print_ascii()