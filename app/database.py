from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = "sqlite:///./finance.db"
engine = create_engine(database_url, connect_args={"check_same_thread": False})
SessionaLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionaLocal()
    try:
        yield db
    finally:
        db.close()