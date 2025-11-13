from fastapi import HTTPException, status, Response
from sqlmodel import Session, select
from .models import PublicationIn, PublicationDb


def create_publication(session: Session, pub_in: PublicationIn):
    pub = PublicationDb.model_validate(pub_in)
    session.add(pub)
    session.commit()
    session.refresh(pub)
    return pub


def get_all_publications(session: Session):
    return session.exec(select(PublicationDb)).all()


def get_publication_by_id(session: Session, pub_id: int):
    pub = session.get(PublicationDb, pub_id)
    if not pub:
        raise HTTPException(
            detail="publication not found", status_code=status.HTTP_404_NOT_FOUND
        )
    return pub


def delete_publication_by_id(session: Session, pub_id: int):
    pub = session.get(PublicationDb, pub_id)
    if not pub:
        raise HTTPException(
            detail="publication not found", status_code=status.HTTP_404_NOT_FOUND
        )
    session.delete(pub)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
