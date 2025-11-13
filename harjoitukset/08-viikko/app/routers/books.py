from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.models import BookIn, BookDb, BookSingle
from ..database import books_crud as crud
from ..database.database import get_session

router = APIRouter(prefix="/books", tags=["books"])


@router.get("", response_model=list[BookDb])
def get_all_books(*, session: Session = Depends(get_session), author_id: int = -1):
    return crud.get_all_books(session, author_id)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=BookSingle)
def create_book(*, session: Session = Depends(get_session), book_in: BookIn):
    return crud.create_book(session, book_in)


@router.get("/{book_id}", response_model=BookSingle)
def get_book_by_id(*, session: Session = Depends(get_session), book_id: int):
    return crud.get_book_by_id(session, book_id)


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_by_id(*, session: Session = Depends(get_session), book_id: int):
    return crud.delete_book_by_id(session, book_id)
