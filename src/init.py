
from httpx import AsyncClient, URL

from src.config import API


api_url = URL(scheme="http", host=API.HOST.value, port=API.PORT.value)


def session_factory() -> AsyncClient:
    session = AsyncClient(base_url=api_url)
    return session

