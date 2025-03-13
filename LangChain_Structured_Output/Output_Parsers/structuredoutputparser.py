from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
load_dotenv()

model = ChatGroq(model="mixtral-8x7b-32768")

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 abou the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 abou the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 abou the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 3 fact about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.invoke({'topic': 'black-hole'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

## NOW USING CHAINS
chain = template | model | parser

final_result = chain.invoke({'topic': 'black-hole'})
print(final_result)