from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

# Set up the Groq model
model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192",  # Example model, choose the right one from Groq
)

messages = [
    SystemMessage(content="You are a helpful assistant!"),
    HumanMessage(content = "Tell me about LanChain"),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)