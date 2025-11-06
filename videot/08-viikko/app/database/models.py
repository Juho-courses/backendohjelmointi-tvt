from sqlmodel import SQLModel, Field


class ShoeBase(SQLModel):
    model: str
    manufacturer: str


class ShoeIn(ShoeBase):
    pass


class ShoeOut(ShoeBase, table=True):
    id: int = Field(default=None, primary_key=True)


class ManufacturerBase(SQLModel):
    name: str


class ManufacturerOut(ManufacturerBase, table=True):
    id: int = Field(default=None, primary_key=True)
