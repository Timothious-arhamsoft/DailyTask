from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.db.database import get_db
from app.models.models import User
from app.schemas.schemas import (NoteCreateSchema, NoteResponseSchema, NoteUpdateSchema)

from app.crud.note_crud import (get_all_notes, get_note_by_id, create_note as crud_create_note, update_note as crud_update_note, delete_note as crud_delete_note)

router = APIRouter(
    prefix="/api/v1/notes",
    tags=["Notes"],
)


@router.get("/", response_model=list[NoteResponseSchema])
def get_notes(db: Session = Depends(get_db),current_user: User = Depends(get_current_user),):
    return get_all_notes(db, current_user.id)


@router.post(
    "/",
    response_model=NoteResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def create_note(
    note: NoteCreateSchema,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return crud_create_note(db=db, note=note, owner_id=current_user.id)


@router.get("/{note_id}", response_model=NoteResponseSchema)
def get_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    note = get_note_by_id(db, note_id, current_user.id)

    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )

    return note


@router.put("/{note_id}", response_model=NoteResponseSchema)
def update_note(
    note_id: int,
    note_update: NoteUpdateSchema,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    note = get_note_by_id(db, note_id, current_user.id)

    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )

    return crud_update_note(db, note, note_update)


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    note = get_note_by_id(db, note_id, current_user.id)

    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )

    crud_delete_note(db, note)