from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough, RunnableBranch
load_dotenv() 

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}.",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Summarize this report {report}.",
    input_variables=['report']
)

model = ChatGroq(model="deepseek-r1-distill-qwen-32b")

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>200, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({'topic':'Pak vs India'})

print(result)

