
from uuid import UUID
from .base import Request


class SendMessageScheme(Request):
    text: str
    chat_uuid: UUID