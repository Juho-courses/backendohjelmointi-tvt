from fastapi import APIRouter, status, Depends
from sqlmodel import Session
from ..database.database import get_session

from ..database import publications_crud as crud
from ..database.models import PublicationDb, PublicationIn

router = APIRouter(prefix="/publications", tags=["publications"])


@router.get("", response_model=list[PublicationDb])
def get_all_publications(*, session: Session = Depends(get_session)):
    return crud.get_all_publications(session)


@router.get("/{pub_id}", response_model=PublicationDb)
def get_publication_by_id(*, session: Session = Depends(get_session), pub_id: int):
    return crud.get_publication_by_id(session, pub_id)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=PublicationDb)
def create_publication(
    *, session: Session = Depends(get_session), pub_in: PublicationIn
):
    return crud.create_publication(session, pub_in)


@router.delete("/{pub_id}", response_model=PublicationDb)
def delete_publication_by_id(*, session: Session = Depends(get_session), pub_id: int):
    return crud.delete_publication_by_id(session, pub_id)
