import os
import json
from datetime import datetime
from dotenv import load_dotenv

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import OutputFixingParser
from langchain_core.output_parsers import JsonOutputParser

from utils import save_structured_json
from schema import NoticeList

# Load env
load_dotenv()

# -----------------------------
# LLM Setup
# -----------------------------
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


parser = JsonOutputParser(pydantic_object=NoticeList)
fixed_parser = OutputFixingParser.from_llm(llm=model, parser=parser)


template = PromptTemplate(
    template="""You are given scraped page contents from a website. 
Extract notices of today's date {date_ad} and return only JSON with the following fields: 
- title: the title text (no HTML tags)
- description: the notice description (plain text, no HTML)
- date: the date of the notice
- file_url: the absolute URL of any associated file or image (if available, otherwise leave blank)

Include all fields; if missing leave blank.

HTML Content:
{context}
""",
    input_variables=["context", "date_ad"],
)


def process_websitewise_scraped():
    date_str = datetime.now().strftime("%Y-%m-%d")
    scraped_folder = os.path.join("notices", date_str)

    if not os.path.exists(scraped_folder):
        print(f"No scraped data found for {date_str}")
        return

    for file in os.listdir(scraped_folder):
        if file.endswith(".json"):
            file_path = os.path.join(scraped_folder, file)
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                website_name = data.get("name", file.replace(".json", ""))
                content = data.get("content", "")
                if not content:
                    continue

                # Run LLM
                context = content
                chain = template | model | fixed_parser
                try:
                    structured_result = chain.invoke(
                        {"context": context, "date_ad": date_str}
                    )
                    save_structured_json(website_name, structured_result)
                except Exception as e:
                    print(f"Error processing {website_name}: {e}")


if __name__ == "__main__":
    process_websitewise_scraped()
