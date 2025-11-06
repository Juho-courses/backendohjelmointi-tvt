from fastapi import APIRouter, status, Depends
from sqlmodel import Session

from ..database import shoes_crud
from ..database.models import ShoeOut, ShoeIn
from ..database.database import get_session

router = APIRouter(prefix="/shoes", tags=["shoes"])


@router.get("", response_model=list[ShoeOut])
def get_all_shoes(*, session: Session = Depends(get_session), manufacturer: str = ""):
    return shoes_crud.get_all_shoes(session, manufacturer)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ShoeOut)
def create_new_shoe(*, session: Session = Depends(get_session), shoe_in: ShoeIn):
    return shoes_crud.create_new_shoe(session, shoe_in)


@router.get("/{shoe_id}", response_model=ShoeOut)
def get_shoe_by_id(*, session: Session = Depends(get_session), shoe_id: int):
    return shoes_crud.get_shoe_by_id(session, shoe_id)


@router.delete("/{shoe_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_shoe_by_id(*, session: Session = Depends(get_session), shoe_id: int):
    return shoes_crud.delete_shoe_by_id(session, shoe_id)
