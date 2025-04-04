from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
# Chat Template
chat_template = ChatPromptTemplate(
    [
        ('system', "You are a helpful Customer support agent"),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human', '{query}')
    ]
)

chat_history = []
# Load chat history
with open('chat_history.txt') as file:
    chat_history.extend(file.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke(
    {
        'chat_history': chat_history,
        'query': "Where is my refund?",
    }
)

print(prompt)