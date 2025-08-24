import os
from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser

from pydantic import BaseModel, Field
from typing import Literal


class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Give the sentiment of the feedback"
    )


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

str_parser = StrOutputParser()
json_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment fo the following feedback in positive or negative: {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": json_parser.get_format_instructions()},
)

classifier_chain = prompt1 | model | json_parser

# print(classifier_chain.invoke({"feedback": "This product is wow"}))

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback: {feedback}",
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback: {feedback}",
    input_variables=["feedback"],
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | str_parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | str_parser),
    RunnableLambda(lambda x: "could not find sentiment"),
)

chain = classifier_chain | branch_chain

print(chain.invoke({"feedback": "This is a beautiful product. I just love it."}))

# chain.get_graph().print_ascii()
