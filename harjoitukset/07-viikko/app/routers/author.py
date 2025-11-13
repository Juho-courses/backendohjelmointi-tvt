from fastapi import APIRouter, status
from ..database.models import AuthorIn, AuthorDb
from ..database import authors_crud as crud

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get("", response_model=list[AuthorDb])
def get_all_authors():
    return crud.get_all_authors()


@router.post("", status_code=status.HTTP_201_CREATED, response_model=AuthorDb)
def create_author(author_in: AuthorIn):
    return crud.create_author(author_in)


@router.get("/{author_id}", response_model=AuthorDb)
def get_author_by_id(author_id: int):
    return crud.get_author_by_id(author_id)


@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_author_by_id(author_id: int):
    return crud.delete_author_by_id(author_id)
