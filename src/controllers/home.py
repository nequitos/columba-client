
from uuid import UUID
from typing import Any, Callable

from flet import Page, ListView
from src.session import BaseSession, BaseWebSocket
from src.models import HomeModel
from src.config import HOST, PORT



class HomeController:
    def __init__(
        self,
        model: HomeModel,
        session: BaseSession
    ) -> None:
        self.__model = model
        self.__session = session
        self.__chat_ws: BaseWebSocket | None = None

    @property
    def uuid(self):
        return self.__model.uuid

    @property
    def username(self):
        return self.__model.username

    async def get_chats(self, page: int, size: int) -> list[dict[str, Any]]:
        response = await self.__session.get(
            "/chat/", params={"page": page, "size": size}
        )

        return response["items"]

    async def get_chat_messages(self, page: int, size: int, chat_uuid: UUID) -> list[dict[str, Any]]:
        response = await self.__session.get(
            f"/chat/messages/{chat_uuid}", params={
                "page": page,
                "size": size
            }
        )

        return response["items"]

    async def set_me_info(self) -> dict[str, Any] | bool:
        response = await self.__session.get("/account/me")

        if response:
            self.__model.uuid = response["uuid"]
            self.__model.username = response["username"]
            return True
        else:
            return False

    async def open_chat_ws(
        self,
        chat_uuid: UUID,
        recipient_uuid: UUID,
        add_msg_cb: Callable[..., Any]
    ):
        ws = BaseWebSocket(
            uri=f"ws://{HOST}:{PORT}/chat/ws/{chat_uuid}/{recipient_uuid}",
            access_token=self.__session.auth.token
        )
        await ws.connect()
        self.__chat_ws = ws

        while True:
            message = await ws.recv_bytes()
            print(message)
            if message:
                add_msg_cb(
                    message["sender_username"],
                    message["text"],
                    message["account_uuid"]
                )

    async def send_message(self, message: str):
        await self.__chat_ws.send(message)

    #
    # async def get_chats(self) -> list[dict[str, Any]] | bool:
    #     response = await self.__session.get("/account/chats")
    #
    #     if response:
    #         return response
    #     else:
    #         return False
    #
    # async def get_chat(self, uuid: UUID) -> dict[str, Any] | bool:
    #     response = await self.__session.get("/chat", params={"uuid": uuid})
    #
    #     if response:
    #         return response
    #     else:
    #         return False
    #
    # async def send_message(self, chat_uuid: UUID, text: str) -> bool:
    #     response = await self.__session.post("/chat/send_message", json={"chat_uuid": chat_uuid, "text": text})
    #
    #     if response:
    #         return True
    #     else:
    #         return False