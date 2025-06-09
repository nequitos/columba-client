
from .base import Validator
from uuid import UUID


class HomeModel:
    access_token: str
    uuid: UUID
    username: str
