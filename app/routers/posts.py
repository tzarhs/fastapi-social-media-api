from typing import List, Optional

from .. import models, schemas, oauth2
from fastapi import  HTTPException, Response, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db

router = APIRouter(
    prefix="/posts",
    tags = ["Posts"]
)

@router.get("/", response_model = List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), limit: int = 2,skip:int = 0,search: Optional[str] = ""):
    # curr.execute("""SELECT * FROM posts""")
    # posts = curr.fetchall()


    #RAW SQL -> SELECT *, COUNT(votes.post_id) AS votes FROM posts (db.query(models.Post),func.count(models.Vote.post_id).label("votes")) 
    #LEFT JOIN votes (.join(models.Vote) 
    #ON posts.id = votes.post_id (models.Vote.post_id == models.Post.id)) 
    #GROUP BY posts.id (.group_by(models.Post.id))
    results = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter = True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
 
    return results

@router.post('/',status_code=201, response_model = schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # curr.execute("""INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    # new_post = curr.fetchone()

    # #To save the changes to the database
    # conn.commit()

    new_post = models.Post(user_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    
    return new_post

@router.get('/{id}', response_model = schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db)):
    # curr.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    # post = curr.fetchone()

    post = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter = True).group_by(models.Post.id).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=404, detail=f"post with id: {id} does not exist")
   
    return  post

@router.delete('/{id}', status_code=204)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # curr.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id),))
    # post = curr.fetchone()
    # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None :
        raise HTTPException(status_code=404, detail=f"post with id: {id} does not exist")

    if post.first().user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform requested action")   

    post.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=204)

@router.put('/{id}', response_model = schemas.Post   )
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # curr.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",(post.title,post.content,post.published,str(id)))
    # updated_post = curr.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id  == id)

    post = post_query.first()


    if post == None:
        raise HTTPException(status_code=404, detail=f"post with id: {id} does not exist")

    if post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform requested action") 

    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    
   
    return  post_query.first()

