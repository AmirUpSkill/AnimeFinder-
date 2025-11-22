import uuid 
from datetime import datetime 
from typing import List 
from sqlalchemy import String , Text , DateTime , func 
from sqlalchemy.dialects.postgresql import UUID 
from sqlalchemy.orm import Mapped , mapped_column 
from pgvector.sqlalchemy import Vector 
from app.db.base import Base 

class Animal(Base):
    __tablename__ = "animals"
    # --- Primary Key --- 
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )
    # --- Metadata --- 
    name: Mapped[str] = mapped_column(String(255),nullable=False)
    # --- Description : The Content We Search Against --- 
    description: Mapped[str] = mapped_column(Text , nullable=False)
    # --- Image Reference (MinIO) --- 
    image: Mapped[str] = mapped_column(String(255),nullable=False)
    # --- The AI Brain (Vector Embedding ) --- 
    embedding: Mapped[List[float]] = mapped_column(Vector(768),nullable=True)
    # --- TimesStamps --- 
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True),onupdate=func.now())
    def __repr__(self):
        return f"Animal(id={self.id}, name={self.name}, description={self.description}, image={self.image}, embedding={self.embedding}, created_at={self.created_at}, updated_at={self.updated_at})"