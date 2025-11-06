from fastapi import status, APIRouter
from ..database.models import ManufacturerBase, ManufacturerOut
from ..database import manufacturers_crud as crud


router = APIRouter(prefix="/manufacturers", tags=["manufacturers"])


@router.get("", response_model=list[ManufacturerOut])
def get_manufacturers(manufacturer: str = ""):
    return crud.get_manufacturers(manufacturer)


@router.post("", response_model=ManufacturerOut, status_code=status.HTTP_201_CREATED)
def create_new_manufacturer(manu_in: ManufacturerBase):
    return crud.create_new_manufacturer(manu_in)


@router.get("/{manufacturer_id}", response_model=ManufacturerOut)
def get_manufacturer_by_id(manufacturer_id: int):
    return crud.get_manufacturer_by_id(manufacturer_id)


@router.delete("/{manufacturer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_manufacturer_by_id(manufacturer_id: int):
    return crud.delete_manufacturer_by_id(manufacturer_id)
