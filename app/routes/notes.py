from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from starlette import status

from app.database import Note, get_db_session
from app.schema import NoteCreate, NoteRead

notes_router = APIRouter(prefix="/notes", tags=["Notes"])


@notes_router.get("/", response_model=list[NoteRead])
def get_notes(db: Session = Depends(get_db_session)):
    notes = db.exec(select(Note)).all()
    return notes


@notes_router.get("/{note_id}", response_model=NoteRead)
def get_note(note_id: int, db: Session = Depends(get_db_session)):
    note = db.get(Note, note_id)
    if not note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )
    return note


@notes_router.post("/", status_code=status.HTTP_201_CREATED)
def create_note(note: NoteCreate, db: Session = Depends(get_db_session)):
    new_note = Note(title=note.title, content=note.content)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note.model_dump()


@notes_router.patch("/{note_id}", response_model=NoteRead)
def update_note(note_id: int, note: NoteCreate, db: Session = Depends(get_db_session)):
    db_note = db.get(Note, note_id)
    if not db_note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note Not Found"
        )

    db_note.title = note.title
    db_note.content = note.content
    db.commit()
    db.refresh(db_note)

    return db_note.model_dump()


@notes_router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: Session = Depends(get_db_session)):
    db_note = db.get(Note, note_id)
    if not db_note:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Note not found"
        )

    db.delete(db_note)
    db.commit()
