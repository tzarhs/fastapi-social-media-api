
from app.routers.votes import vote

from .database import engine
from . import models
from fastapi import FastAPI
from .routers import posts, users, auth, votes

from app.config import settings

# models.Base.metadata.create_all(bind=engine)

app =  FastAPI()


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")
def read_root():
    return {"Hello": "Welcome to my API"}

