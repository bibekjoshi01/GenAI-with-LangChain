import os
from dotenv import load_dotenv
from typing import TypedDict

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="conversational",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
    max_new_tokens=256,
    do_sample=False,
    temperature=0.7,
    top_p=0.9,
)

model = ChatHuggingFace(llm=llm)


class Review(TypedDict):
    summary: str
    sentiment: str


structured_model = model.with_structured_output(Review)

result = structured_model.invoke(
    """This movie is just great and wow. I love it."""
)

print(result)
print(result['summary'])
print(result['sentiment'])
