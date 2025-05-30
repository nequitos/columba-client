
import logging

from .base import BaseSession, HTTPStatusError, RequestError


logger = logging.getLogger(__name__)


class OAuth2Session:
    def __init__(
        self,
        session: BaseSession,
        token_endpoint_uri: str,
        username: str | None = None,
        password: str | None = None,
        grant_type: str | None = None,
        scopes: list[str] = [],
        client_id: str | None = None,
        client_secret: str | None = None
    ) -> None:
        if grant_type is None:
            grant_type = "password"

        self.data = dict(
            username=username,
            password=password,
            scopes=scopes,
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret
        )

        self.token_endpoint_uri = token_endpoint_uri
        self._session = session

    def set_credentials(
        self,
        username: str,
        password: str,
        client_id: str | None = None,
        client_secret: str | None = None
    ) -> None:
        self.data.update(
            username=username,
            password=password,
            client_id=client_id,
            client_secret=client_secret
        )

    async def authenticate_session(self) -> bool:
        access_token = await self.get_access_token()
        self._session.headers["Authorization"] = f"Bearer {access_token}"
        self._session.cookies.set("access_token", access_token)

        return True

    async def get_access_token(self) -> str:
        try:
            resp = await self._session.client.post(
                self.token_endpoint_uri,
                data=self.data,
                headers={"Content-Type": "application/x-www-form-urlencoded"}
            )
            resp.raise_for_status()
            return resp.json()["access_token"]
        except HTTPStatusError:
            raise
        except RequestError:
            raise