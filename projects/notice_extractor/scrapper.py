from langchain_community.document_loaders import WebBaseLoader

WEBSITE_LIST = [
    "http://exam.ioe.edu.np/",
    "https://psc.sudurpashchim.gov.np/notice_list",
]


def scrap_notices():
    loader = WebBaseLoader(web_path=WEBSITE_LIST)

    docs = loader.load()

    return docs