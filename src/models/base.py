
from flet import Page
from src.session import BaseSession


class ModelObject:
    def __init__(self, page: Page, session: BaseSession) -> None:
        self._page = page
        self._session = session