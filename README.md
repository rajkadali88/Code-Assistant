# Code Assistant – GenAI-Powered Developer Support Tool

A natural language interface to your codebase, powered by LangChain, FastAPI, and RAG. This assistant helps developers query their codebase using plain English and receive context-aware answers, retrieved from vectorized documentation and processed through LLMs.


## Features

**Natural Language to Code Insight** – Ask questions like “What does `login_user` do?” and get clear answers.
**RAG-Enhanced Retrieval** – Uses FAISS to retrieve relevant code snippets and documentation before generating responses.
**Modular Architecture** – Clean separation of frontend, backend, and services for scalability.
**Containerized Deployment** – Docker + Compose for easy setup and multi-service orchestration.
**Streamlit UI** – Intuitive interface for developers to interact with the assistant.



## Tech Stack

Python, Langchain, FastAPI, Streamlit, FAISS, Docker, Ollama, Pydantic



## Installation

git clone https://github.com/rajkadali88/Code-Assistant.git
cd Code-Assistant
docker-compose up --build 


- Access the frontend at: http://localhost:8501
- Backend API at: http://localhost:8000/chat



