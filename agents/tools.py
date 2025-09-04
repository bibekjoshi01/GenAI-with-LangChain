from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

search_result = search_tool.invoke("What is capital city of Nepal")

print(search_result)
