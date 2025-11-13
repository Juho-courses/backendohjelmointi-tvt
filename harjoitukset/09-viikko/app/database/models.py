from sqlmodel import SQLModel, Field, Relationship


class BandBase(SQLModel):
    name: str
    year_of_foundation: int


class BandIn(BandBase):
    pass


class BandDb(BandBase, table=True):
    id: int = Field(default=None, primary_key=True)
    releases: list["PublicationDb"] = Relationship(back_populates="band")


class BandSingle(SQLModel):
    id: int
    name: str
    releases: list["PublicationNoBand"] | None


class PublicationBase(SQLModel):
    name: str
    release_year: int
    band_id: int


class PublicationIn(PublicationBase):
    pass


class PublicationDb(PublicationBase, table=True):
    id: int = Field(default=None, primary_key=True)
    band_id: int = Field(default=None, foreign_key="banddb.id")
    band: BandDb | None = Relationship(back_populates="releases")


class PublicationNoBand(SQLModel):
    name: str
    release_year: int
