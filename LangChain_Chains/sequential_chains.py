from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a detail report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Pitch the 5 pointer summary from the report {report}.",
    input_variables=['report']
)

model = ChatGroq(model="mixtral-8x7b-32768")

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

response = chain.invoke({'topic': 'Jobs Shortage in Pakistan'})

print(response)

chain.get_graph().print_ascii() # graphical representation of the chain