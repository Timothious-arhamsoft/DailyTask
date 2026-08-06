from sqlalchemy import (Column, Integer, String, Boolean, ForeignKey)
from sqlalchemy.orm import relationship
from db.database import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    # One Category -> Many Tasks
    tasks = relationship("Task", back_populates="category")

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False, nullable=False)
    created_at = Column(String, nullable=False)
    priority = Column(Integer, default=1, nullable=False)
    # Foreign Key
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    # Relationship
    category = relationship("Category", back_populates="tasks")
