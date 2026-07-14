from typing import Optional
from urllib import response

from .database import SessionDep, create_db_and_tables
from .models import Post

from fastapi import FastAPI, HTTPException, Response
from fastapi.params import Body
from sqlmodel import select, Session
from httpx import post
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time


app =  FastAPI()   

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/posts")
def create_post(post: Post, session: SessionDep) -> Post:
    # session.add(post)
    # session.commit()
    # session.refresh(post)
    return post


def find_post(id):
    for post in get_posts:
        if post['id'] == id:
            return post
        
def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/")
def read_root():
    return {"Hello": "Welcome to my API"}

@app.get("/posts")
def get_posts():
    curr.execute("""SELECT * FROM posts""")
    posts = curr.fetchall()
    return {"data": posts}

@app.post('/posts',status_code=201)
def create_posts(post:Post):
    curr.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    new_post = curr.fetchone()

    #To save the changes to the database
    conn.commit()
    
    return {"data": new_post}

@app.get('/posts/{id}')
def get_post(id: int):
    curr.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    post = curr.fetchone()

    if not post:
        raise HTTPException(status_code=404, detail=f"post with id: {id} does not exist")
   
    return {"post_details": post}

@app.delete('/posts/{id}', status_code=204)
def delete_post(id: int):
    curr.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id),))
    post = curr.fetchone()
    conn.commit()

    if post == None :
        raise HTTPException(status_code=404, detail=f"post with id: {id} does not exist")
    
    return Response(status_code=204)

@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    curr.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",(post.title,post.content,post.published,str(id)))
    updated_post = curr.fetchone()
    conn.commit()

    if updated_post == None:
        raise HTTPException(status_code=404, detail=f"post with id: {id} does not exist")
    
   
    return {'data': updated_post}