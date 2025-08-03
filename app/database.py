import os
from typing import Optional

from dotenv import load_dotenv
from sqlmodel import Field, Session, SQLModel, create_engine

load_dotenv(override=True)

engine = create_engine(os.environ.get("DATABASE_URL", "sqlite:///./data/dev.db"))


def get_db_session():
    with Session(engine) as session:
        yield session


class Note(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(default="Untitled")
    content: Optional[str] = Field(default="")


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(default="")
    address: str = Field(default="")
    age: int = Field(default=None)
