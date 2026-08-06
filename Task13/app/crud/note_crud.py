from sqlalchemy.orm import Session

from app.models.models import Note
from app.schemas.schemas import NoteCreateSchema, NoteUpdateSchema


def get_all_notes(db: Session):
    return db.query(Note).all()


def get_note_by_id(db: Session, note_id: int):
    return db.query(Note).filter(Note.id == note_id).first()


def create_note(db: Session, note: NoteCreateSchema):
    new_note = Note(
        title=note.title,
        body=note.body,
        category_id=note.category_id,
        owner_id=1  
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note


def update_note(db: Session, db_note: Note, note: NoteUpdateSchema):
    if note.title is not None:
        db_note.title = note.title

    if note.body is not None:
        db_note.body = note.body

    if note.category_id is not None:
        db_note.category_id = note.category_id

    db.commit()
    db.refresh(db_note)

    return db_note


def delete_note(db: Session, db_note: Note):
    db.delete(db_note)
    db.commit()