
from uuid import UUID
from typing import Any
import asyncio

from src.session import BaseSession
from src.models import HomeModel

from src.session.schemes import chat as chat_schemes


class HomeController:
    def __init__(
        self,
        model: HomeModel,
        session: BaseSession
    ) -> None:
        self.__model = model
        self.__session = session


    @property
    def uuid(self):
        return self.__model.uuid

    async def set_me_info(self) -> dict[str, Any] | bool:
        response = await self.__session.get("/account/me")

        if response:
            self.__model.uuid = response["uuid"]
            self.__model.first_name = response["first_name"]
            self.__model.last_name = response["last_name"]

            return True
        else:
            return False

    async def get_chats(self) -> list[dict[str, Any]] | bool:
        response = await self.__session.get("/account/chats")

        if response:
            return response
        else:
            return False

    async def get_chat(self, uuid: UUID) -> dict[str, Any] | bool:
        response = await self.__session.get("/chat", params={"uuid": uuid})

        if response:
            return response
        else:
            return False

    async def send_message(self, chat_uuid: UUID, text: str) -> bool:
        response = await self.__session.post("/chat/send_message", json={"chat_uuid": chat_uuid, "text": text})

        if response:
            return True
        else:
            return False