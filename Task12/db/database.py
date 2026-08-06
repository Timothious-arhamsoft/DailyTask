from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite database
DATABASE_URL = "sqlite:///tasks.db"

# Create Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}, 
    echo=True 
)

# Create Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for all ORM models
Base = declarative_base()


# Dependency used in FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()