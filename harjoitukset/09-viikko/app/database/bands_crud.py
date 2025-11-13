from fastapi import HTTPException, status, Response
from sqlmodel import Session, select
from .models import BandIn, BandDb


def create_band(session: Session, band_in: BandIn):
    band = BandDb.model_validate(band_in)
    session.add(band)
    session.commit()
    session.refresh(band)
    return band


def get_all_bands(session: Session, band_name):
    if band_name:
        return session.exec(select(BandDb).where(BandDb.name == band_name)).all()
    return session.exec(select(BandDb)).all()


def get_band_by_id(session: Session, band_id: int):
    band = session.get(BandDb, band_id)
    if not band:
        raise HTTPException(
            detail="band not found", status_code=status.HTTP_404_NOT_FOUND
        )
    return band
