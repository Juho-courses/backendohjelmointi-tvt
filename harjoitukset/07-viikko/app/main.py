from fastapi import FastAPI
from .routers import books, author

app = FastAPI()
app.include_router(books.router)
app.include_router(author.router)
