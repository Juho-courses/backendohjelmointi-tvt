from sqlmodel import SQLModel, Field, Relationship


class AuthorBase(SQLModel):
    name: str


class AuthorIn(AuthorBase):
    pass


class AuthorDb(AuthorBase, table=True):
    id: int = Field(default=None, primary_key=True)
    books: list["BookDb"] = Relationship(back_populates="author")


class AuthorSingle(SQLModel):
    id: int
    name: str
    books: list["BookNoAuthor"] | None


class BookBase(SQLModel):
    name: str
    author_id: int


class BookIn(BookBase):
    pass


class BookDb(BookBase, table=True):
    id: int = Field(default=None, primary_key=True)
    author_id: int | None = Field(default=None, foreign_key="authordb.id")
    author: AuthorDb | None = Relationship(back_populates="books")


class BookNoAuthor(SQLModel):
    id: int
    name: str


class BookSingle(SQLModel):
    id: int
    name: str
    author: AuthorDb | None
