
from .base import Validator
from uuid import UUID


class HomeModel:
    uuid: UUID
    first_name: str
    last_name: str
