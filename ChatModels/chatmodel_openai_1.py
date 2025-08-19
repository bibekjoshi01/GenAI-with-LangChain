from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

chat_model = ChatOpenAI(model="gpt-4", temperature=1, max_completion_tokens=1000)

resut = chat_model.invoke("What is the capital city of Nepal?")

print(resut)
