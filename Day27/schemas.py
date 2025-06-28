from pydantic import BaseModel

# Pydantic schema for creating a book
class BookCreate(BaseModel):
    title: str
    author: str
    isbn: str
    publication_year: int

# Pydantic schema for returning a book
class BookOut(BookCreate):
    id: int

    class Config:
        orm_mode = True
