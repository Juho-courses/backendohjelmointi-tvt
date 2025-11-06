from fastapi import APIRouter, status

from ..database import shoes_crud
from ..database.models import ShoeOut, ShoeIn

router = APIRouter(prefix="/shoes", tags=["shoes"])


@router.get("", response_model=list[ShoeOut])
def get_all_shoes(manufacturer: str = ""):
    return shoes_crud.get_all_shoes(manufacturer)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ShoeOut)
def create_new_shoe(shoe_in: ShoeIn):
    return shoes_crud.create_new_shoe(shoe_in)


@router.get("/{shoe_id}", response_model=ShoeOut)
def get_shoe_by_id(shoe_id: int):
    return shoes_crud.get_shoe_by_id(shoe_id)


@router.delete("/{shoe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shoe_by_id(shoe_id: int):
    return shoes_crud.delete_shoe_by_id(shoe_id)
