from langchain.vectorstores import FAISS 
from langchain.embeddings import OllamaEmbeddings

def create_faiss_index(docs):
    embeddings = OllamaEmbeddings(model='all-minilm',base_url='http://host.docker.internal:11434')
    return FAISS.from_documents(docs,embeddings)

