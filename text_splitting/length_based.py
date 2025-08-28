from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader("./data.txt", encoding="utf-8")

docs = loader.load()

splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0, separator="")

result = splitter.split_documents(docs)

print(result[0].page_content)

