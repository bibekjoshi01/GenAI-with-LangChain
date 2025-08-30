# Maximal Marginal Relevance

# How can we pick results that are not only relevant to the query but also different from each other?

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document


documents = [
    Document(page_content="LangChain helps developers build LLM application easily."),
    Document(
        page_content="Chroma is a vector database optimized for LLM-based search."
    ),
    Document(page_content="Embeddings convert text into high dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

embedding_model = OpenAIEmbeddings()

vector_store = FAISS.from_documents(
    documents=documents,
    embedding=embedding_model,
)

# Type: MMR
retriever = vector_store.as_retriever(
    search_type="mmr", search_kwargs={"k": 2, "lambda_mult": 1}
)

query = "What is chroma used for?"

results = retriever.invoke(query)

print(results)
