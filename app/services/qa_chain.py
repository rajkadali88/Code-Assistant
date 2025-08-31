from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from app.config import MODEL_NAME 

llm = ChatOllama(model='llama3.2:1b',base_url='http://host.docker.internal:11434')

template = """
You are a codebase assistant. Use the following code snippets to answer the question.
{code_snippets}

Question: {question}
"""

prompt = PromptTemplate(
    input_variables=['code_snippets','question'],
    template=template 
)

qa_chain = prompt | llm 

def get_answer(code_snippets,question):
    return qa_chain.invoke({'code_snippets':code_snippets,'question':question})