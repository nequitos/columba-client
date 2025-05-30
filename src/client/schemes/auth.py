
from .base import Response, Request


class CreateAccount(Request):
    first_name: str
    last_name: str
    email: str
    password: str


class OAuth2(Request):
    username: str
    password: str
    grant_type: str | None = None
    scopes: list[str] | None = ["me", "items"]
    client_id: str | None = None
    client_secret: str | None = None

