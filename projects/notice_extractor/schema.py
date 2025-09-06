from pydantic import BaseModel, Field
from typing import List


# Pydantic schema for notices
class Notice(BaseModel):
    title: str = Field(description="Title of the notice")
    description: str = Field(description="Description of the notice")
    date: str = Field(description="Date of the notice")
    file_url: str = Field(description="absolute Url of the notice file, image (any one)")


class NoticeList(BaseModel):
    notices: List[Notice]
