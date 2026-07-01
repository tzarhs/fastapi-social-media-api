from typing import Optional
from urllib import response

from fastapi import FastAPI, HTTPException, Response
from fastapi.params import Body
from httpx import post
from pydantic import BaseModel
from random import randrange

app =  FastAPI()    

# Schema
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]

def find_post(id):
    for post in my_posts:
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
    return {"data": my_posts}

@app.post('/posts',status_code=201)
def create_posts(post:Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get('/posts/{id}')
def get_post(id: int, response:Response):
    post = find_post(id)
   
    if not post:
        raise HTTPException(status_code=404, detail=f"post with id: {id} was not found")
        # response.status_code = 404
        # return {"message": f"post with id: {id} was not found"}
    
    return {"post_details": post}

@app.delete('/posts/{id}', status_code=204)
def delete_post(id: int):
    index = find_index_post(id)
    if not index:
        raise HTTPException(status_code=404, detail=f"post with id: {id} does not exist")
    
    my_posts.pop(index)

    return Response(status_code=204)

@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=404, detail=f"post with id: {id} does not exist")
    
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {'data': post_dict}