import logging

import inject
from app.api.schema.login import AuthResponse
from app.core.error import ApplicationError
from app.core.settings import CoreSettings
from app.core.utils import create_access_token
from app.core.schema import JWTUser
from app import constants

logger = logging.getLogger(__name__)


class AuthenticatorService:
    def __init__(self, current_user_id: str | None = None):
        self.settings: CoreSettings = inject.get_injector().get_instance(CoreSettings)

    async def verify_password(self, email: str, password: str) -> AuthResponse:
        # For demo purpose this implementation is done
        if email == "atul" and password == "atul":
            access = {}
            # Update this code to pull actions from user_actions table
            data = JWTUser(
                id=email,
                email=email,
                sub=str(email),
            ).dict()

            access["token"] = create_access_token(data)
            access["t_type"] = "access"
            access["user_id"] = email
            access["is_revoked"] = False
            return AuthResponse(
                email=email,
                access_token=access.get("token"),
            )

        raise ApplicationError(response_code=constants.HTTP_401_UNAUTHORIZED, message="User password is wrong")

    async def logout(self) -> None:
        """
        :return:
        """
        pass
