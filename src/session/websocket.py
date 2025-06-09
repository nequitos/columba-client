
import pickle
from typing import Any
import json

from .auth import OAuth2
from websockets.asyncio.client import connect, ClientConnection


class BaseWebSocket:
    IS_CONNECT: bool = False

    def __init__(self, uri: str, access_token: str):
        self._uri = uri
        self.__access_token = access_token
        self.__connection: ClientConnection | None = None

    async def __aenter__(self):
        await self.connect()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()

    async def connect(self) -> None:
        headers = {
            "Authorization": f"Bearer {self.__access_token}"
        }
        self.__connection = await connect(self._uri, additional_headers=headers)
        self.IS_CONNECT = True

    async def disconnect(self):
        await self.__connection.close()
        self.IS_CONNECT = False

    async def recv(self):
        return await self.__connection.recv()

    async def recv_bytes(self):
        return pickle.loads(await self.__connection.recv())[0]

    async def recv_json(self):
        return json.loads(await self.__connection.recv())

    async def send(self, message: Any):
        await self.__connection.send(message=message, text=True)


if __name__ == "__main__":
    from auth import OAuth2
    import asyncio

    loop = asyncio.get_event_loop()

    oauth = OAuth2(
        scheme="http",
        host="localhost",
        port=8000,
        token_endpoint_uri="/auth/token",
        username="ne.quit.osx@gmail.com",
        password="string",
        scopes=["me", "items"]
    )
    access_token = loop.run_until_complete(oauth.get_access_token())

    ws = BaseWebSocket(
        "ws://localhost:8000/chat/ws",
        access_token=access_token
    )

    loop.run_until_complete(ws.connect())
    loop.run_until_complete(ws.recv())

