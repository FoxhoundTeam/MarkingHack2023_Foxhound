from fastapi import APIRouter, Depends

from app import schemes
from app.services.auth import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Авторизация"],
)


@router.post("/sign-in/", response_model=schemes.Token, summary="Авторизация")
def sign_in(auth_data: schemes.Credentials, auth_service: AuthService = Depends(AuthService)):
    return auth_service.authenticate_user(auth_data.username, auth_data.password)
