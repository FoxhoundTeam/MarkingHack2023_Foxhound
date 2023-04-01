from fastapi import Depends
from sqlalchemy.orm import Session

from app import database


class BaseDBService:
    def __init__(self, session: Session = Depends(database.get_session)):
        self.session = session

    def _save_obj(self, obj):
        self.session.add(obj)
        self.session.commit()
