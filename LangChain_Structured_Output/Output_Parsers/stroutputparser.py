"""
Practical implementation of Str Output Parser & why we prefer the stroutputparser on result.content
"""
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
load_dotenv()

model = ChatGroq(model="mixtral-8x7b-32768")

# 1st prompt -> detailed prompt
template1 = PromptTemplate(
    template = "Write a detail report on {topic}",
    input_variable=['topic']
)


# 2nd prompt -> summary
template2 = PromptTemplate(
    template = "Write a 5 line summary on the following text. \n {text}",
    input_variable=['text']
)

# USING ONLY result.content

# prompt1 = template1.invoke({"topic": "Black-Hole"})

# result1 = model.invoke(prompt1)

# prompt2 = template2.invoke({'text': result1.content})

# result2 = model.invoke(prompt2)

# print(result2.content)


# NOW USING THE STR-OUTPUT-PARSERS (Chains is used)

from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': "Black Hole"})

print(result)