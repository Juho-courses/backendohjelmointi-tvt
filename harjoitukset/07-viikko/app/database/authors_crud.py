from fastapi import HTTPException, status, Response
from .models import AuthorIn, AuthorDb

authors = [
    {"id": 0, "name": "author 0"},
    {"id": 1, "name": "author 1"},
]


def get_all_authors():
    return authors


def create_author(author_in: AuthorIn):
    new_id = max([b["id"] for b in authors]) + 1
    author = AuthorDb(id=new_id, **author_in.model_dump())
    authors.append(author.model_dump())
    return author


def get_author_by_id(author_id: int):
    tmp_authors = [b for b in authors if b["id"] == author_id]
    if len(tmp_authors) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="author not found")

    return tmp_authors[0]


def delete_author_by_id(author_id: int):
    tmp_index = -1
    for i, b in enumerate(authors):
        if b["id"] == author_id:
            tmp_index = i
            break

    if tmp_index == -1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="author not found")

    del authors[tmp_index]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
