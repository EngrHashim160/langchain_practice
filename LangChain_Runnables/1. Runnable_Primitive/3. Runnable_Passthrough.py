from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough
load_dotenv()

prompt1 = PromptTemplate(
    template="Write a joke about {topic} in 1-2 lines",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="explain the following joke {text} in 2-5 lines only",
    input_variables=['text']
)
model = ChatGroq(model="deepseek-r1-distill-qwen-32b")

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1, model, parser)
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic': 'cricket'})
print(result['joke'])
print(result['explanation'])