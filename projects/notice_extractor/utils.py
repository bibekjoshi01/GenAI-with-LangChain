import os
import json
from datetime import datetime
from bs4 import BeautifulSoup, Comment

OUTPUT_ROOT = "notices"
STRU_OUTPUT_ROOT = "structured_notices"


def clean_body_html(raw_html: str) -> str:
    soup = BeautifulSoup(raw_html, "html.parser")

    # Remove script and style tags
    for tag in soup(["script", "style"]):
        tag.decompose()

    # Remove comments
    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    # Keep only essential attributes
    allowed_attrs = {"a": ["href", "title"], "img": ["src", "alt"]}
    for tag in soup.find_all(True):
        if tag.name in allowed_attrs:
            tag.attrs = {
                k: v for k, v in tag.attrs.items() if k in allowed_attrs[tag.name]
            }
        else:
            tag.attrs = {}

    return str(soup)


def save_json(website_name: str, data: dict):
    date_str = datetime.now().strftime("%Y-%m-%d")
    safe_name = "".join([c if c.isalnum() else "_" for c in website_name])
    folder_path = os.path.join(OUTPUT_ROOT, date_str)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"{safe_name}.json")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def save_structured_json(website_name: str, data: dict):
    date_str = datetime.now().strftime("%Y-%m-%d")
    safe_name = "".join([c if c.isalnum() else "_" for c in website_name])
    folder_path = os.path.join(STRU_OUTPUT_ROOT, date_str)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"{safe_name}.json")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
