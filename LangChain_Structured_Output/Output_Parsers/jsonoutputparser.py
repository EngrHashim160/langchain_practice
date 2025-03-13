from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()

model = ChatGroq(model="mixtral-8x7b-32768")

parser = JsonOutputParser()
template = PromptTemplate(
    template = "Write a detail report on {topic} \n {format_instruction}",
    input_variable=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
) 

# prompt = template.invoke({'topic': "Life in Pakistan"})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)


# USING CHAINS
chain = template | model | parser
final_result = chain.invoke({'topic': "Life in Pakistan"})
print(final_result)
print(type(final_result))
