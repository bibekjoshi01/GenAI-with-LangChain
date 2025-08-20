from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(BASE_DIR, "chat_history.txt")

chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful customer support agent"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{query}"),
    ]
)

# load chat history
chat_history = []

with open(file_path) as f:
    chat_history.extend(f.readlines())


prompt = chat_template.invoke({"chat_history": chat_history, "query": "Where is my refund?"})

print(prompt)