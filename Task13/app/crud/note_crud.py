from sqlalchemy.orm import Session
from app.models.models import Note


def get_all_notes(db: Session):
    return db.query(Note).all()