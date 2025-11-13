from fastapi import HTTPException, status, Response
from sqlmodel import Session, select
from .models import AuthorIn, AuthorDb


def get_all_authors(session: Session):
    return session.exec(select(AuthorDb)).all()


def create_author(session: Session, author_in: AuthorIn):
    author = AuthorDb.model_validate(author_in)
    session.add(author)
    session.commit()
    session.refresh(author)
    return author


def get_author_by_id(session: Session, author_id: int):
    author = session.get(AuthorDb, author_id)
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="author not found")

    return author


def delete_author_by_id(session: Session, author_id: int):
    author = session.get(AuthorDb, author_id)

    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="author not found")

    session.delete(author)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
