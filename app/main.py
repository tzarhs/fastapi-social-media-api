from typing import Optional,List
from urllib import response

from .database import engine,SessionLocal,get_db
from . import models, schemas,utils

from fastapi import FastAPI, HTTPException, Response, Depends
from fastapi.params import Body
from sqlmodel import select, Session

from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .routers import posts, users, auth

models.Base.metadata.create_all(bind=engine)

app =  FastAPI()


app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"Hello": "Welcome to my API"}

