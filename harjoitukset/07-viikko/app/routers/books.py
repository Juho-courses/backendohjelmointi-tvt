from fastapi import APIRouter, status
from ..database.models import BookIn, BookOut
from ..database import books_crud as crud

router = APIRouter(prefix="/books", tags=["books"])


@router.get("", response_model=list[BookOut])
def get_all_books(author_id: int = -1):
    return crud.get_all_books(author_id)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=BookOut)
def create_book(book_in: BookIn):
    return crud.create_book(book_in)


@router.get("/{book_id}", response_model=BookOut)
def get_book_by_id(book_id: int):
    return crud.get_book_by_id(book_id)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_by_id(book_id: int):
    return crud.delete_book_by_id(book_id)
