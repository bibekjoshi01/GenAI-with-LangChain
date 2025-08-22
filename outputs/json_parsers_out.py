import os
from dotenv import load_dotenv
import json

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

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

parser = JsonOutputParser()

template1 = PromptTemplate(
    template="Give me the name, age and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = template1 | model | parser

result = chain.invoke(input={})

print(result)