from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Pydantic model for a Book
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    genre: Optional[str] = None

# In-memory "database"
books_db: List[Book] = []

# --------------------
# 📘 Create a new book
# --------------------
@app.post("/books/", response_model=Book)
def create_book(book: Book):
    for existing_book in books_db:
        if existing_book.id == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists.")
    books_db.append(book)
    return book

# ----------------------------
# 📗 Get all books (read all)
# ----------------------------
@app.get("/books/", response_model=List[Book])
def read_books():
    return books_db

# ---------------------------
# 📙 Get a book by its ID
# ---------------------------
@app.get("/books/{book_id}", response_model=Book)
def read_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# ---------------------------------
# 📕 Update a book (by ID)
# ---------------------------------
@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            books_db[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# --------------------------
# ❌ Delete a book by ID
# --------------------------
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books_db):
        if book.id == book_id:
            del books_db[index]
            return {"message": f"Book with ID {book_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
