import os

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
    max_new_tokens=256,
    do_sample=False,
    temperature=0.7,
    top_p=0.9,
)


model = ChatHuggingFace(llm=endpoint)

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}", input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "AI/ML"})

chain.get_graph().print_ascii()

print(result)