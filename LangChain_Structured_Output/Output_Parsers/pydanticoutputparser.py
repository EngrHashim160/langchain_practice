from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
load_dotenv()

model = ChatGroq(model="mixtral-8x7b-32768")

class Person(BaseModel):
    name: str = Field(description='Name of the person'),
    age: int = Field(gt=18, description="Age of the person"),
    city: str = Field(description="Name of the city the person belongs to.")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'Genarate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables= {'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({'place': 'pakistani'})
# print(prompt)
# result = model.invoke(prompt)

# final_result = parser.parse(result.content)


## USING CHAINS
chain = template | model | parser
final_result = chain.invoke({'place': 'pakistani'})
print(final_result)