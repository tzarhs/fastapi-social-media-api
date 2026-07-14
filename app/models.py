from sqlmodel import Field, SQLModel

class Post(SQLModel, table=True):
    __tablename__ = "posts"

    id: int | None = Field(default=None, primary_key=True, nullable=False)
    title: str = Field(index=True, nullable=False)
    content: str = Field(index=True, nullable=False)
    published: bool = Field(default=True)
     