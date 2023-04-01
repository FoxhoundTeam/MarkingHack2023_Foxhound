from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

from app.config import settings

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

engine = create_engine(settings.database_uri, pool_pre_ping=True, echo=True)
SessionLocal = sessionmaker(autocommit=False, expire_on_commit=False, autoflush=False, bind=engine)


@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


@as_declarative()
class BaseWithID:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id = Column(Integer, autoincrement=True, primary_key=True, index=True, unique=True)

    def __str__(self):
        return f"<{type(self).__name__} id={self.id}>"


def get_session() -> "Session":
    with SessionLocal() as session:
        yield session
