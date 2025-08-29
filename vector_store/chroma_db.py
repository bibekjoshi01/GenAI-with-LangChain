from langchain.vectorstores import Chroma
from langchain.schema import Document


doc1 = Document(page_content="Bibek Joshi", metadata={"rollno": 1})


vector_store = Chroma(
    embedding_function=..., persist_directory="chroma_db", collection_name="sample"
)

# Adding documentes to database
vector_store.add_documents([doc1])

# View documents
vector_store.get(include=["embeddings", "documents", "metadatas"])

# Searching documents (2 results)
vector_store.similarity_search(query="Who is Bibek?", k=2)

