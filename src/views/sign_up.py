
from flet import (
    View
)

from src.enums import view as view_enums
from src.models import SignUpModel
from src.controllers.container import SignUpContainer


class SignUpView(View):
    def __init__(self, model: SignUpModel) -> None:
        super().__init__(
            route=view_enums.Route.SIGN_UP
        )
        self.__model = model

        self._container = SignUpContainer(model)
        self.controls = [
            self._container
        ]
