from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.auth.router import router as auth_router
from app.db import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(auth_router)


@app.get("/")
async def read_root():
    return "Healthy"
