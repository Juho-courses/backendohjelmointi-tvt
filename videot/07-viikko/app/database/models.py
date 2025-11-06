from pydantic import BaseModel


class ShoeBase(BaseModel):
    model: str
    manufacturer: str


class ShoeIn(ShoeBase):
    pass


class ShoeOut(ShoeBase):
    id: int


class ManufacturerBase(BaseModel):
    name: str


class ManufacturerOut(ManufacturerBase):
    id: int
