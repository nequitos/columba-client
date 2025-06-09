
from .base import Request, Response


class SignUpRequest(Request):
    email: str


class VerifyEmailCodeRequest(Request):
    email: str
    code: str
    password: str
    username: str


class AuthRequest(Request):
    username: str
    password: str
    scopes: list[str] = ["me", "items"]



class TokenResponse(Response):
    access_token: str
    token_type: str