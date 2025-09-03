from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import (
    HuggingFaceEmbeddings,
)
from langchain_community.vectorstores import FAISS

DATA_PATH = "data/"
DB_FAISS_PATH = "vectorstore/db_faiss"


# Data Loading
def load_pdf_files(path):
    loader = DirectoryLoader(path, glob="*pdf", loader_cls=PyPDFLoader)

    return loader.load()


documents = load_pdf_files(path=DATA_PATH)


# Chunking
def create_chunks(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    return text_splitter.split_documents(extracted_data)


text_chunks = create_chunks(extracted_data=documents)


# Embedding
def get_embedding_model():
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embedding_model


embedding_model = get_embedding_model()

db = FAISS.from_documents(text_chunks, embedding_model)
db.save_local(DB_FAISS_PATH)
