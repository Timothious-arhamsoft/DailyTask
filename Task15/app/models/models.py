
from sqlalchemy import Integer, String, Column, Text, DateTime, ForeignKey
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
from app.db.database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(256), nullable=False)
    role = Column(String(20), nullable=False, default='user')

    notes = relationship("Note", back_populates="owner")

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
    
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    notes = relationship("Note", back_populates="category")

    def __repr__(self):
        return f"<Category(name='{self.name}')>"
    
class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    body = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=True, index=True)

    owner = relationship("User", back_populates="notes")
    category = relationship("Category", back_populates="notes")

    @property
    def username(self):
        return self.owner.username if self.owner else None

    def __repr__(self):
        return f"<Note(title='{self.title}', created_at='{self.created_at}')>"


    