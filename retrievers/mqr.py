# Multi Query Retriever

# Sometimes a single query might not capture all the ways information is phraased in your documents.

# It reduces the ambiguity in query: ex: How can I stay healthy?

from langchain.retrievers.multi_query import MultiQueryRetriever

multiquery_retriever = MultiQueryRetriever.from_llm(retriever=..., llm=...)
