from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
import os

# Load API key from .env file
load_dotenv()

# Set up the Groq model
model = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-8b-8192",  # Example model, choose the right one from Groq
)

chat_history = []
while(True):
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == "exit":
        break
    response = model.invoke(chat_history)
    chat_history.append(response.content)
    print(f"AI: {response.content}")
