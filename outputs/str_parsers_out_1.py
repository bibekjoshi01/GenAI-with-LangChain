import os
from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

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


template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a 2 line summary on the following text. /n {text}",
    input_variables=["text"],
)

# prompt1 = template1.invoke({"topic": "black hole"})

# result1 = model.invoke(prompt1)

# prompt2 = template2.invoke(
#     {
#         "text": "I am bibek joshi. I study in class 10. I work hard. I have many friends. I am developer at early age. I like computer science and mathematics."
#     }
# )

# result2 = model.invoke(prompt2)

# print(result1.content)
# print(result2.content)

parser = StrOutputParser()

chain = template1 | model | parser

result = chain.invoke({"topic": "black hole"})

print(result)