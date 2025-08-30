from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=2, lang='en')

query = 'history on nepal and end of rana regime'

docs = retriever.invoke(query)

print(docs)

for i, doc in docs:
    print(doc.page_content)