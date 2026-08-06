from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.schemas import (
    UserCreateSchema,
    UserResponseSchema,
)

from app.crud.user_crud import (
    create_user,
    get_user_by_email,
)

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"],
)


@router.post(
    "/",
    response_model=UserResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def register_user(
    user: UserCreateSchema,
    db: Session = Depends(get_db),
):
    existing = get_user_by_email(db, user.email)

    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    return create_user(db, user)