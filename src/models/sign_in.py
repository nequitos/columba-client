
from .base import ModelObject
from flet import (
    ControlEvent,
    TextField,
    IconButton,
    TextCapitalization,
    KeyboardType
)

from src.enums import view as view_enums


class SignInModel(ModelObject):
    async def on_sign_up(self, event: ControlEvent) -> None:
        self._page.go(view_enums.Route.SIGN_UP)

    async def on_sign_in(self, event: ControlEvent) -> None:
        self._page.go(view_enums.Route.HOME)

    async def on_back(self, event: ControlEvent) -> None:
        self._page.go(view_enums.Route.INDEX)