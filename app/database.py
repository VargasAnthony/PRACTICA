from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATA_BASE = "sqlite:///./database.db"

engine = create_engine(DATA_BASE, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
