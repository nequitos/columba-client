
from .base import Validator


class SignUp(Validator):
    first_name: str
    last_name: str
    email: str
    password: str


class SignIn(Validator):
    username: str
    password: str


class OAuth2(Validator):
    username: str
    password: str
    grant_type: str | None = None
    scopes: list[str] = []
    client_id: str | None = None
    client_secret: str | None = None