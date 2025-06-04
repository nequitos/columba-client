
from typing import Any
from uuid import UUID

from .base import BaseSession


class Session:
    def __init__(
        self,
        session: BaseSession
    ) -> None:
        self._session = session

    async def chat_create(self, text: str, recipient_uuid: UUID):
        await self._session.post(
            "/chat/create", json={"text": text, "recipient_uuid": recipient_uuid}
        )

    async def send_message(self, text: str, chat_uuid: UUID):
        await self._session.post(
            "/chat/send_message", json={"text": text, "chat_uuid": UUID}
        )

    async def chats(self) -> list[dict[str, Any]]:
        response = await self._session.get(
            "/account/chats"
        )
        return response

    async def chat_messages(self, chat_uuid: UUID):
        response = await self._session.get(
            "/chat", params={"uuid": chat_uuid}
        )
        return response


    async def me(self) -> dict[str, Any]:
        return await self._session.get("/account/me")