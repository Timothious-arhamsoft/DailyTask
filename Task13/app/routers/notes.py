from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.crud.note_crud import get_all_notes
from app.schemas.schemas import NoteResponseSchema

router = APIRouter(
    prefix="/api/v1/notes",
    tags=["Notes"]
)


@router.get("/", response_model=list[NoteResponseSchema])
def get_notes(db: Session = Depends(get_db)):
    return get_all_notes(db)