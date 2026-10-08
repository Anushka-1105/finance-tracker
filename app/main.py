from fastapi import FastAPI

from .database import engine, Base
from . import models
from .routers import transactions

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance Tracker API")
app.include_router(transactions.router)


@app.get("/")
def home():
    return {"message": "Hello, Finance Tracker!"}


@app.get("/about")
def about():
    return {"app": "Finance Tracker", "by": "Anushka"}