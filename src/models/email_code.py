

from .base import ModelObject
from flet import ControlEvent

from src.enums import view as view_enums



class EmailCodeModel(ModelObject):
    def on_confirm(self, event: ControlEvent, code: str) -> None:
        self._page.go(view_enums.Route.HOME)

    def on_back(self, event: ControlEvent) -> None:
        self._page.go(view_enums.Route.SIGN_UP)
