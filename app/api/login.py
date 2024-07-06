from app.api.schema import login
from app.core.router import APIRouter
from fastapi import Form
from app.service.authenticator import AuthenticatorService

router = APIRouter(tags=["Authentication"])


@router.post("/token", response_model=login.AuthResponse, include_in_schema=False)
async def get_token(username: str = Form(), password: str = Form()) -> login.AuthResponse:
    """
    This API is used by OpenAPI specification only, not meant to be used by the other users
    :param username:
    :param password:
    :return:
    """
    service = AuthenticatorService()
    return await service.verify_password(username, password)
