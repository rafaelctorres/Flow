from fastapi import FastAPI
from sqlalchemy import text

from app.db import SessionLocal

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/health/db")
def health_db():
    session = SessionLocal()
    session.execute(text("select 1"))
    session.close()
    return {"database": "ok"}