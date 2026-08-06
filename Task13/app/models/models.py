
from sqlalchemy import Integer, String, Column

from app.db.database import Base
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    role = Column(String(20), nullable=False, default='user')

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"
    
class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<Category(name='{self.name}')>"
    