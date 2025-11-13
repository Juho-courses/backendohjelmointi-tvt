from fastapi import FastAPI
from .routers import bands, publications
from contextlib import asynccontextmanager
from .database.database import create_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(bands.router)
app.include_router(publications.router)
