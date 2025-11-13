from pydantic import BaseModel


class BookBase(BaseModel):
    name: str
    author: int


class BookIn(BookBase):
    pass


class BookOut(BookBase):
    id: int


class AuthorBase(BaseModel):
    name: str


class AuthorIn(AuthorBase):
    pass


class AuthorDb(AuthorBase):
    id: int
