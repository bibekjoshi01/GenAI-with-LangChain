from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model='gpt-4', temperature=1)

resut = chat_model.invoke("What is the capital city of Nepal?")

print(resut)