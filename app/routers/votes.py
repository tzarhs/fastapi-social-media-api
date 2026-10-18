from fastapi import  HTTPException, Response, Depends, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas, oauth2, database

router = APIRouter(
    prefix="/vote",
    tags = ["Vote"]
)

@router.post('/', status_code=201)
def vote(vote: schemas.Vote, db : Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    if(vote.dir == 1):
        