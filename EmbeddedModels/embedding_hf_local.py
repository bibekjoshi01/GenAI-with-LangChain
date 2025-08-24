from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ["HF_HOME"] = "/Users/bibekjoshi01/Desktop/Langchain/models"

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text = ["My name is bibek", "This is student"]

# vector = embedding.embed_query(text)
vector = embedding.embed_documents(texts=text)

print(vector)
