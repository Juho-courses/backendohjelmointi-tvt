from fastapi import FastAPI

app = FastAPI()

books = [
    {"name": "Book1", "author": 1},
    {"name": "Book2", "author": 2},
    {"name": "Book3", "author": 1},
]


@app.get("/books")
def get_all_books(author_id: int = None):
    if author_id is None:
        return books
    else:
        return [b for b in books if b['author'] == author_id]


@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    return books[book_id]
