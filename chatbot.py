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

while(True):
    user_input = input("You: ")
    if user_input == "exit":
        break
    response = model.invoke(user_input)
    print(f"AI: {response.content}")
