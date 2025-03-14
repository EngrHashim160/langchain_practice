from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
load_dotenv()


model1 = ChatGroq(model="mixtral-8x7b-32768")
model2 = ChatGroq(model_name="llama3-8b-8192")

prompt1 = PromptTemplate(
    template="Generate a short & simple notes from the document provided. {document}",
    input_variables=['document']
)

prompt2 = PromptTemplate(
    template="Generate a quiz of 10 questions from the document provided. {document}",
    input_variables=['document']
)

prompt3 = PromptTemplate(
    template="Merge the notes & quiz into a single document.\n notes->{notes} and quiz->{quiz}",
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        'notes': prompt1 | model1 | parser,
        'quiz': prompt2 | model2 | parser
    }
)

merged_chain = prompt3 | model1 | parser

chain = parallel_chain | merged_chain

document_text = """
    Introduction to LangChain

LangChain is a powerful framework designed to simplify the development of applications powered by large language models (LLMs). It enables developers to integrate different components such as models, prompts, chains, memory, and agents to build more advanced, context-aware, and interactive AI-driven applications.

Core Components of LangChain

Models
LangChain provides support for multiple LLM providers, including OpenAI, Hugging Face, and Cohere. These models can be integrated easily into applications using LangChain's model abstraction.

Prompts
Prompts are templates used to interact with language models. LangChain enables the creation of dynamic and structured prompts that adapt to user inputs and application requirements.

Chains
A chain is a sequence of calls to language models or other components. Chains allow for structured workflows where different steps in an AI pipeline can be executed sequentially or conditionally.

Memory
Memory helps applications maintain context over a conversation or multiple interactions. It enables AI models to recall previous exchanges, making interactions more coherent and engaging.

Indexes
LangChain supports indexing techniques to store and retrieve information efficiently. It enables vector databases, document stores, and search functionalities that improve information retrieval for AI applications.

Agents
Agents in LangChain allow AI models to perform reasoning and decision-making based on user input and external data. They can execute different tasks, call APIs, and interact with databases dynamically.

Tools and Plugins
LangChain provides integrations with various tools, including APIs, databases, search engines, and cloud storage, enhancing AI applications' functionality.

Use Cases of LangChain

Conversational AI

Chatbots and virtual assistants

AI-powered customer support systems

Document Processing

Summarization of large documents

Automated report generation

Search and Retrieval Systems

Smart search engines

Context-aware document retrieval

AI-Powered Agents

Task automation using AI

API-driven AI workflows

Code Generation and Assistance

AI-assisted programming tools

Automatic code documentation

Building a Simple LangChain Application

Here’s an example of how to create a simple chatbot using LangChain and OpenAI’s GPT-4 model:

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

# Initialize the model
chat = ChatOpenAI(model_name="gpt-4", temperature=0.7)

# Create a user query
user_message = HumanMessage(content="What is LangChain?")

# Get response
response = chat([user_message])
print(response.content)

This basic example demonstrates how LangChain simplifies interactions with LLMs while providing flexibility for complex applications.

Advanced Features

Multimodal Support

Combining text, image, and other modalities in AI interactions

Fine-Tuning and Customization

Using custom models for domain-specific applications

Scalability

Deploying AI applications on cloud platforms with load balancing

Security and Compliance

Implementing authentication, encryption, and access control for sensitive applications

Conclusion

LangChain provides a comprehensive framework for building AI-powered applications with ease. Whether you're developing chatbots, document processors, search engines, or intelligent agents, LangChain simplifies integration and deployment while allowing for advanced customization. As AI continues to evolve, LangChain stands as a crucial tool in harnessing th
"""
result = chain.invoke({'document': document_text})

print(result)
chain.get_graph().print_ascii() # graphical representation of the chain