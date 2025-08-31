from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router

app = FastAPI(title='codebase QA Assistant')


app.add_middleware(
    CORSMiddleware,
    allow_methods=['*'],
    allow_origins=['*']
)

app.include_router(router)