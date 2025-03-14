from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
load_dotenv()


# Pydantic class
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="Give the sentiment of the feedback.")

model = ChatGroq(model="mixtral-8x7b-32768")
parser1 = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative.\n {feedback} \n {format_instruction}", 
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)


classifier_chain = prompt1 | model | parser2

result = classifier_chain.invoke({'feedback': 'The phone is fantastic.'}).sentiment

print(result)