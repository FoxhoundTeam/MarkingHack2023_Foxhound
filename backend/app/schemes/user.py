from app.schemes.base import CamelModel


class BaseUser(CamelModel):
    username: str


class UserVerifyToken(BaseUser):
    id: int


class UserORM(UserVerifyToken):
    class Config:
        orm_mode = True
