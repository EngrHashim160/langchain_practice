import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# File to store chat history
CHAT_HISTORY_FILE = "chat_history.txt"

# Function to load chat history from file
def load_chat_history():
    if os.path.exists(CHAT_HISTORY_FILE):
        with open(CHAT_HISTORY_FILE, "r", encoding="utf-8") as file:
            return file.read().strip()
    return ""

# Function to save new messages to chat history
def save_to_chat_history(user_input, ai_response):
    with open(CHAT_HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"User: {user_input}\nAI: {ai_response}\n\n")

# Initialize Chat Model (Groq)
llm = ChatGroq(model_name="mixtral-8x7b-32768")

# Define Prompt Template (Including History)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly chatbot that remembers previous conversations."),
    ("human", "{history}\nUser: {user_input}"),
])

def chat():
    print("🤖 AI Chatbot (Type 'exit' to quit)\n")

    # Load previous chat history
    chat_history = load_chat_history()

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("👋 Chat ended. Your history is saved!")
            break

        # Format the prompt with history
        formatted_prompt = prompt.format(history=chat_history, user_input=user_input)

        # Get AI response
        response = llm.invoke(formatted_prompt)

        # Display AI response
        print(f"AI: {response}")

        # Update chat history
        chat_history += f"User: {user_input}\nAI: {response}\n\n"
        save_to_chat_history(user_input, response)

if __name__ == "__main__":
    chat()
