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
    return get_all_notes_admin(db)