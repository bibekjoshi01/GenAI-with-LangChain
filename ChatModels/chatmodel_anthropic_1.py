from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv

load_dotenv()

chat_model = ChatAnthropic(model="claude-5-5-sonnet-20241022", temperature=1, max_completion_tokens=1000)

resut = chat_model.invoke("What is the capital city of Nepal?")

print(resut)
