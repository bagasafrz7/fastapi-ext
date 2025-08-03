from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    content: str


class NoteRead(BaseModel):
    id: int
    title: str


class UsersRead(BaseModel):
    id: int
    name: str
    address: str
    age: int


class UsersCreate(BaseModel):
    name: str
    address: str
    age: int
