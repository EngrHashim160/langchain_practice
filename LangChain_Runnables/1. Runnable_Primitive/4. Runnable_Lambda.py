from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough
load_dotenv() 

prompt = PromptTemplate(
    template="Write a joke about {topic}.",
    input_variables=['topic']
)
model = ChatGroq(model="deepseek-r1-distill-qwen-32b")
parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

def word_count(text):
    return len(text.split())

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'words': RunnableLambda(word_count) # also RunnableLambda(lambda x: len(x.split())) best
})

final_chain = joke_gen_chain | parallel_chain # same as RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'AI'})

print(result)