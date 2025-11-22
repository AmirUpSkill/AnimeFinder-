import uuid 
from datetime import datetime 
from typing import List , Optional 
from pydantic import BaseModel , Field , ConfigDict

# --- Base Schema --- 
class AnimalBase(BaseModel):
    name: str = Field(..., min_length=2 , max_length=100 , description="Name of the animal")
    description: str = Field(..., min_length=10, description="Description of the animal")

# --- Create Schema --- 
class AnimalCreate(AnimalBase):
    pass

# --- Response Schema --- 
class AnimalResponse(AnimalBase):
    id: uuid.UUID = Field(..., description="ID of the animal")
    created_at: datetime = Field(..., description="Creation date of the animal")
    updated_at: Optional[datetime] = Field(None, description="Update date of the animal")

    model_config = ConfigDict(from_attributes=True)

# ----------------------------------------------------------
# --- Search Schemas ---
# ----------------------------------------------------------
class SearchRequest(BaseModel):
    query: str = Field(..., min_length=3 , description="The user's search query description")
    limit: int = Field(10 , ge=1 , le=50 , description="The number of results to return")
class SearchResultItem(AnimalBase):
    similarity_score: float = Field(..., description="Similarity score of the search result")
class SearchResponse(BaseModel):
    results: List[SearchResultItem]
    inference_time: float = Field(..., description="Time taken to calculate embeddings and search (in seconds)")