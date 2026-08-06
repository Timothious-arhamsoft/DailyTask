from sqlalchemy.orm import Session

from app.models.models import User
from app.schemas.schemas import UserCreateSchema


def create_user(db: Session, user: UserCreateSchema) -> User:
    new_user = User(
        username=user.username,
        email=user.email,
        password_hash=user.password,
        role="user"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()