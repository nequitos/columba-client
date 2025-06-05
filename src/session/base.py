
from typing import Any, Callable
import logging

from httpx import (
    AsyncClient,
    URL,
    HTTPStatusError,
    RequestError,
    BasicAuth
)
from .auth import OAuth2


type JsonDumpsType = dict[str, Any]
type JsonLoadsType = Callable[..., dict[str, Any]]


logger = logging.getLogger(__name__)


class BaseSession:
    def __init__(
        self,
        scheme: Any,
        host: Any,
        port: Any,
        auth: OAuth2
    ) -> None:
        self._client = AsyncClient(
            base_url=URL(scheme=scheme, host=host, port=port), auth=auth
        )
        self.headers = self._client.headers
        self.cookies = self._client.cookies

        self.headers["Content-Type"] = "application/json"

    @property
    def client(self):
        return self._client

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if not self._client.is_closed:
            await self._client.aclose()

    async def get(self, path: str, params: JsonDumpsType | None = None) -> JsonLoadsType:
        try:
            logger.debug(f"Send request with params: {params}")
            resp = await self._client.get(path, params=params)
            resp.raise_for_status()
            return resp.json()
        except HTTPStatusError as exc:
            raise
        except RequestError as exc:
            raise

    async def post(
        self,
        path: str,
        json: JsonDumpsType | None = None,
    ) -> JsonLoadsType:
        try:
            logger.debug(f"Send request with data {json}")
            resp = await self._client.post(path, json=json)
            resp.raise_for_status()
            return resp.json()
        except HTTPStatusError as exc:
            raise
        except RequestError as exc:
            raise

    async def patch(self):
        pass

    async def delete(self):
        pass

    async def put(self):
        pass