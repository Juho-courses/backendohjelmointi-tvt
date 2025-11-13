from fastapi import HTTPException, status, Response
from .models import BookIn, BookOut

books = [
    {"id": 0, "name": "Book1", "author": 1},
    {"id": 1, "name": "Book2", "author": 2},
    {"id": 2, "name": "Book3", "author": 1},
]


def get_all_books(author_id: int = -1):
    if author_id == -1:
        return books
    else:
        return [b for b in books if b['author'] == author_id]


def create_book(book_in: BookIn):
    new_id = max([b["id"] for b in books]) + 1
    book = BookOut(id=new_id, **book_in.model_dump())
    books.append(book.model_dump())
    return book


def get_book_by_id(book_id: int):
    tmp_books = [b for b in books if b["id"] == book_id]
    if len(tmp_books) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="book not found")

    return tmp_books[0]


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
