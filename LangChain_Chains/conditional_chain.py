from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
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

# for positive response
prompt2 = PromptTemplate(
    template="Write an appropriate responne to this positive feedback \n {feedback}",
    input_variables=['feedback']
)

# for negative response
prompt3 = PromptTemplate(
    template="Write an appropriate respone to this negative feedback \n {feedback}",
    input_variables=['feedback']
)

classifier_chain = prompt1 | model | parser2

branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2 | model | parser1),
    (lambda x:x.sentiment=='negative', prompt3 | model | parser1),
    RunnableLambda(lambda x: "Could not find sentiment")

)
final_chain = classifier_chain | branch_chain

response = final_chain.invoke({'feedback': 'Tea is just water.'})

print(response)

final_chain.get_graph().print_ascii()