from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel

app = FastAPI()


class BookBase(BaseModel):
    name: str
    author: int


class BookIn(BookBase):
    pass


class BookOut(BookBase):
    id: int


books = [
    {"id": 0, "name": "Book1", "author": 1},
    {"id": 1, "name": "Book2", "author": 2},
    {"id": 2, "name": "Book3", "author": 1},
]


@app.get("/books", response_model=list[BookOut])
def get_all_books(author_id: int = -1):
    if author_id == -1:
        return books
    else:
        return [b for b in books if b['author'] == author_id]


@app.post("/books", status_code=status.HTTP_201_CREATED, response_model=BookOut)
def create_book(book_in: BookIn):
    new_id = max([b["id"] for b in books]) + 1
    book = BookOut(id=new_id, **book_in.model_dump())
    books.append(book.model_dump())
    return book


@app.get("/books/{book_id}", response_model=BookOut)
def get_book_by_id(book_id: int):
    tmp_books = [b for b in books if b["id"] == book_id]
    if len(tmp_books) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="book not found")

    return tmp_books[0]


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_by_id(book_id: int):
    tmp_index = -1
    for i, b in enumerate(books):
        if b["id"] == book_id:
            tmp_index = i
            break

    if tmp_index == -1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="book not found")

    del books[tmp_index]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
