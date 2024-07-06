from app.core.schema import BaseRequestSchema


class AuthRequest(BaseRequestSchema):
    email: str
    password: str


class AuthResponse(BaseRequestSchema):
    email: str | None = None
    access_token: str
