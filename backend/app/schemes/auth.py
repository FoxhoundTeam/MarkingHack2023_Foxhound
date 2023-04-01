from app.schemes.base import CamelModel


class Token(CamelModel):
    access_token: str


class Credentials(CamelModel):
    username: str
    password: str


class ChangePassword(CamelModel):
    password: str
