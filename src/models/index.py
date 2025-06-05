
from .base import ModelObject
from flet import ControlEvent

from src.enums import view as view_enums


class IndexModel(ModelObject):
    async def on_start(self, event: ControlEvent):
        self._page.go(view_enums.Route.SIGN_IN)