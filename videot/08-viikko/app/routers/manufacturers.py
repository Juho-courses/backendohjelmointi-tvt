from fastapi import status, APIRouter, Depends
from sqlmodel import Session
from ..database.models import ManufacturerBase, ManufacturerOut
from ..database import manufacturers_crud as crud

from ..database.database import get_session


router = APIRouter(prefix="/manufacturers", tags=["manufacturers"])


@router.get("", response_model=list[ManufacturerOut])
def get_manufacturers(*, session: Session = Depends(get_session), manufacturer: str = ""):
    return crud.get_manufacturers(session, manufacturer)


@router.post("", response_model=ManufacturerOut, status_code=status.HTTP_201_CREATED)
def create_new_manufacturer(*, session: Session = Depends(get_session), manu_in: ManufacturerBase):
    return crud.create_new_manufacturer(session, manu_in)


@router.get("/{manufacturer_id}", response_model=ManufacturerOut)
def get_manufacturer_by_id(*, session: Session = Depends(get_session), manufacturer_id: int):
    return crud.get_manufacturer_by_id(session, manufacturer_id)


@router.delete("/{manufacturer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_manufacturer_by_id(*, session: Session = Depends(get_session), manufacturer_id: int):
    return crud.delete_manufacturer_by_id(session, manufacturer_id)
