from fastapi import Depends, FastAPI, HTTPException
from scalar_fastapi import get_scalar_api_reference
from sqlmodel import Session, select

from app.database import Note, get_db_session
from app.schema import NoteCreate, NoteRead

app = FastAPI()


@app.get("/notes", response_model=list[NoteRead])
def get_notes(db: Session = Depends(get_db_session)):
    notes = db.exec(select(Note)).all()
    return notes


@app.get("/notes/{note_id}", response_model=NoteRead)
def get_note(note_id: int, db: Session = Depends(get_db_session)):
    note = db.get(Note, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.post("/notes")
def create_note(note: NoteCreate, db: Session = Depends(get_db_session)):
    new_note = Note(title=note.title, content=note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note.model_dump()


@app.patch("/notes/{note_id}", response_model=NoteRead)
def update_note(note_id: int, note: NoteCreate, db: Session = Depends(get_db_session)):
    db_note = db.get(Note, note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note Not Found")

    db_note.title = note.title
    db_note.content = note.content
    db.commit()
    db.refresh(db_note)

    return db_note.model_dump()


# def handle_params(limit: int = 10, skip: int = 0, filter: str = None):
#     return {"limit": limit, "skip": skip, "filter": filter}


# @app.get("/notes")
# def get_notes(query: dict = Depends(handle_params)):
#     return {"notes": [], "query": query}


# @app.get("/products")
# def get_products(query: dict = Depends(handle_params)):
#     return {"products": [], "query": query}


@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )
