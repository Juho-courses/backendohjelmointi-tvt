class ManufacturerBase(BaseModel):
    name: str


class ManufacturerOut(ManufacturerBase):
    id: int
