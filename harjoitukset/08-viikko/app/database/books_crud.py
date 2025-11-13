from fastapi import HTTPException, status, Response
from sqlmodel import Session, select
from .models import BookIn, BookDb


def get_all_books(session: Session, author_id: int = -1):
    if author_id != -1:
        return session.exec(select(BookDb).where(BookDb.author == author_id)).all()
    else:
        return session.exec(select(BookDb)).all()


def create_book(session: Session, book_in: BookIn):
    book = BookDb.model_validate(book_in)
    session.add(book)
    session.commit()
    session.refresh(book)
    return book


def get_book_by_id(session: Session, book_id: int):
    book = session.get(BookDb, book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="book not found")

    return book


def delete_book_by_id(session: Session, book_id: int):
    book = session.get(BookDb, book_id)

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="book not found")

    session.delete(book)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
