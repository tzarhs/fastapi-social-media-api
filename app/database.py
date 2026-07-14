from typing import Annotated

from fastapi import Depends
from sqlmodel import  Session, SQLModel, create_engine

from .models import Post

postgres_url = "postgresql+psycopg2://postgres:co3w!da4@localhost/fastapi"

engine = create_engine(postgres_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session



SessionDep = Annotated[Session, Depends(get_session)]




