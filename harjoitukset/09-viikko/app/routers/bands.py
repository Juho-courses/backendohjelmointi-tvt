from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.database import get_session
from ..database import bands_crud as crud
from ..database.models import BandIn, BandDb, BandSingle

router = APIRouter(prefix="/bands", tags=["bands"])


@router.get("", response_model=list[BandDb])
def get_all_bands(
    *, session: Session = Depends(get_session), band_name: str | None = None
):
    return crud.get_all_bands(session, band_name)


@router.get("/{band_id}", response_model=BandSingle)
def get_band_by_id(*, session: Session = Depends(get_session), band_id: int):
    return crud.get_band_by_id(session, band_id)


@router.post("", status_code=status.HTTP_201_CREATED)
def create_band(*, session: Session = Depends(get_session), band_in: BandIn):
    return crud.create_band(session, band_in)
