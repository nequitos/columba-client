
from httpx import AsyncClient


class BaseSession:
    def __init__(self, api_url: str):
        self.__client = AsyncClient(base_url=api_url)
