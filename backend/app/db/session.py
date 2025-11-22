from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker , Session 
from app.core.config import settings 
from typing import Generator 

# --- Here We Create the Database Engine --- 
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True, # --- Here Check the connection is Alive or not ---
    echo=False # --- Here We Disable the SQL Logging ---
)

# --- Here We Create the Session --- 
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
# --- Dependency --- 
def get_db() -> Generator[Session , None , None]:
    """
        Dependency that Creates a new database session for a request 
        and closes it when the request if finished 
    """
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()