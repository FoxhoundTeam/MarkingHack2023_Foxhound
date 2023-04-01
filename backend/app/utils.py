from typing import TYPE_CHECKING, TypeVar, cast

from fastapi import HTTPException
from starlette import status

if TYPE_CHECKING:
    from sqlalchemy.orm.session import Session

    from app.database import Base

T = TypeVar("T")


def get_or_404(session: "Session", model: type["Base"], _id: int, message: str = None):
    obj = session.query(model).get(_id)
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message or "Entity with such id doesn't exist",
        )
    return cast(type(model), obj)
