
from asyncio import sleep

from .base import ModelObject
from flet import (
    Column,
    TextField,
    ElevatedButton
)
from flet import ControlEvent

from src.enums import (
    button as button_enums,
    view as view_enums
)


class SignUpModel(ModelObject):
    def on_send_code(self, event: ControlEvent, email: str):
        self._page.go(view_enums.Route.EMAIL_CODE)

    def on_back(self, event: ControlEvent) -> None:
        self._page.go(view_enums.Route.SIGN_IN)
