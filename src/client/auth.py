
import asyncio
import logging

from httpx import (
    Auth,
    Request,
    Response,
    Client,
    HTTPStatusError,
    RequestError,
    URL
)


logger = logging.getLogger(__name__)


class OAuth2(Auth):
    def __init__(
        self,
        scheme: str,
        host: str,
        port: str,
        token_endpoint_uri: str,
        username: str | None = None,
        password: str | None = None,
        grant_type: str | None = None,
        scopes: list[str] = [],
        client_id: str | None = None,
        client_secret: str | None = None
    ):
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
        self._session = Client(base_url=URL(scheme=scheme, host=host, port=port))
        self._async_lock = asyncio.Lock()
        self.__token: str | None = None

    @property
    def token(self) -> str:
        return self.__token

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

    async def authorize_account(self) -> bool:
        access_token = await self.get_access_token()

        if access_token:
            self.__token = access_token
            return True
        else:
            return False

    async def async_auth_flow(self, request: Request):
        request.headers["Authorization"] = f"Bearer {self.__token}"
        response = yield request

        if response.status_code == 401:
            pass

    async def get_access_token(self) -> str:
        try:
            async with self._async_lock:
                resp = self._session.post(
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

    def build_refresh_request(self):
        pass

    def update_tokens(self, response):
        pass
