from fastapi import APIRouter
import asyncio
from app.models import Query
from app.services import parser,indexer,retriever,qa_chain
from app.config import DATABASE_PATH,TOP_K

router = APIRouter()



docs = parser.load_codebase(DATABASE_PATH)
print(docs)
vectorstore = indexer.create_faiss_index(docs)

@router.post('/chat')
async def ask_codebase(query:Query):
    print("______________________query _______________________",query)
    snippets = retriever.retrieve_snipets(vectorstore,query.question,k=TOP_K)
    print("____________________________snippets______________________-",snippets)
    answer = qa_chain.get_answer(snippets,query.question)
    return {'answer':answer}


    