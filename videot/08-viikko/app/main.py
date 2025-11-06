from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routers import shoes, manufacturers
from .database.database import create_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("startataan")
    create_db()
    yield
    print("sammutetaan")

app = FastAPI(lifespan=lifespan)
app.include_router(shoes.router)
app.include_router(manufacturers.router)
