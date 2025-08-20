from langchain_core.prompts import PromptTemplate


template = PromptTemplate(template="""""", input_variables=[], validate_template=True)

template.save('temp.json')