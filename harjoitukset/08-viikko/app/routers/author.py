from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.models import AuthorIn, AuthorDb, AuthorSingle
from ..database import authors_crud as crud
from ..database.database import get_session

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("", response_model=list[AuthorDb])
def get_all_authors(*, session: Session = Depends(get_session)):
    return crud.get_all_authors(session)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=AuthorDb)
def create_author(*, session: Session = Depends(get_session), author_in: AuthorIn):
    return crud.create_author(session, author_in)


@router.get("/{author_id}", response_model=AuthorSingle)
def get_author_by_id(*, session: Session = Depends(get_session), author_id: int):
    return crud.get_author_by_id(session, author_id)


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author_by_id(*, session: Session = Depends(get_session), author_id: int):
    return crud.delete_author_by_id(session, author_id)
