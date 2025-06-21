from dataclasses import dataclass, field
from typing import Optional, List

@dataclass()
class Book:
    title: str
    author: str
    isbn: str
    publication_year: int
    genre: Optional[str] = None

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Publication year: {self.publication_year}")
        print(f"Genre: {self.genre if self.genre else 'Details not available'}")

Library: List[Book] = [
    Book("Dune", "Frank Herbert", "978-0593099321", 1965, genre="Science fiction"),
    Book("The Alchemist", "Paulo Coelho", "9780061122415", 1988),
    Book("1984", "George Orwell", "9780451524935", 1949, genre="Dystopian"),
    Book("Clean Code", "Robert C. Martin", "9780132350884", 2008, genre="Programming")
]

for Book in Library:
    print("-------------------")
    Book.display_details()