import os
import json
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import OutputFixingParser
from langchain_core.output_parsers import JsonOutputParser

# Load Project Imports
from scrapper import scrap_notices
from schema import NoticeList

# Load environment variables
load_dotenv()

# Setup HuggingFace endpoint
endpoint = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HF_TOKEN"),
    max_new_tokens=1500,
    do_sample=False,
    temperature=0.3,
    top_p=0.9,
)

model = ChatHuggingFace(llm=endpoint)

# Define Parsers
parser = JsonOutputParser(pydantic_object=NoticeList)
fixed_parser = OutputFixingParser.from_llm(llm=model, parser=parser)

# Prompt
template = PromptTemplate(
    template="""You are given scraped page contents from websites. 
Extract notices from them and return only in JSON format (title, description, date) Include these three in all instances if not availble leave blank.

Context:
{context}
""",
    input_variables=["context"],
)

chain = template | model | fixed_parser

# Convert scraped docs to text
docs = scrap_notices()
context = "\n\n".join([d.page_content for d in docs])

# Run chain
result = chain.invoke({"context": context})

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=1)
