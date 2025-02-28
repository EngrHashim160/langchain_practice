from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os

# Load API key from .env file
load_dotenv()

# Set up the Groq model
model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192",  # Example model, choose the right one from Groq
)

chat_history = [
    SystemMessage(content = "You are a helpful Assistant!")
]

while(True):
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content = response.content))
    print(f"AI: {response.content}")

print(chat_history)