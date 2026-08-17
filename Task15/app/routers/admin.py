from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import require_admin
from app.db.database import get_db
from app.models.models import User
from app.schemas.schemas import NoteResponseSchema
from app.crud.note_crud import get_all_notes_admin

router = APIRouter(
    prefix="/api/v1/admin",
    tags=["Admin"],
)


@router.get(
    "/notes",
    response_model=list[NoteResponseSchema],
)
def get_all_notes(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    notes = get_all_notes_admin(db)
    return [
        NoteResponseSchema(
            id=note.id,
            title=note.title,
            body=note.body,
            owner_id=note.owner_id,
            username=note.owner.username if note.owner else None,
            category_id=note.category_id,
            created_at=note.created_at,
            updated_at=note.updated_at,
        )
        for note in notes
    ]