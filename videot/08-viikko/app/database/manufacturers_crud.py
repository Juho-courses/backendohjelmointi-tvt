from fastapi import HTTPException, Response, status
from sqlmodel import Session, select
from .models import ManufacturerBase, ManufacturerOut


def get_manufacturers(session: Session, manufacturer: str):
    if manufacturer == "":
        return session.exec(select(ManufacturerOut)).all()
    else:
        return session.exec(select(ManufacturerOut).where(ManufacturerOut.name == manufacturer)).all()


def create_new_manufacturer(session: Session, manu_in: ManufacturerBase):
    manu = ManufacturerOut.model_validate(manu_in)
    session.add(manu)
    session.commit()
    session.refresh(manu)
    return manu


def get_manufacturer_by_id(session: Session, manufacturer_id: int):
    manu = session.get(ManufacturerOut, manufacturer_id)
    if not manu:
        raise HTTPException(
            status_code=404, detail=f"manufacturer with id {manufacturer_id} not found.")
    return manu


def delete_manufacturer_by_id(session: Session, manufacturer_id: int):
    manu = session.get(ManufacturerOut, manufacturer_id)
    if not manu:
        raise HTTPException(
            status_code=404, detail=f"manufacturer with id {manufacturer_id} not found.")
    session.delete(manu)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
