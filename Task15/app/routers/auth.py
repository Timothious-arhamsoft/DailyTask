from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.schemas import LoginSchema, TokenSchema
from app.crud.user_crud import get_user_by_email
from app.auth.security import (
    verify_password,
    create_access_token,
)

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=TokenSchema,
)
def login(
    credentials: LoginSchema,
    db: Session = Depends(get_db),
):
    # Find user by email
    user = get_user_by_email(db, credentials.email)

    # User doesn't exist
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # Wrong password
    if not verify_password(
        credentials.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    # Generate JWT
    access_token = create_access_token(
        subject=user.id,
        role=user.role,
    )

    return TokenSchema(
        access_token=access_token,
        token_type="bearer",
    )