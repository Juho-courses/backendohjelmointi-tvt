from fastapi import HTTPException, Response, status
from .models import ShoeIn, ShoeOut
from sqlmodel import Session, select


def get_all_shoes(session: Session, manufacturer: str = ""):
    if manufacturer != "":
        return session.exec(select(ShoeOut).where(ShoeOut.manufacturer == manufacturer)).all()
    return session.exec(select(ShoeOut)).all()


def create_new_shoe(session: Session, shoe_in: ShoeIn):
    shoe = ShoeOut.model_validate(shoe_in)
    session.add(shoe)
    session.commit()
    session.refresh(shoe)
    return shoe


def get_shoe_by_id(session: Session, shoe_id: int):
    shoe = session.get(ShoeOut, shoe_id)
    if not shoe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"shoe with id {shoe_id} not found.")
    return shoe


def delete_shoe_by_id(session: Session, shoe_id: int):
    shoe = session.get(ShoeOut, shoe_id)
    if not shoe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"shoe with id {shoe_id} not found.")
    session.delete(shoe)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
