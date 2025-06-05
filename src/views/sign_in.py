
from flet import View

from src.enums import view as view_enums
from src.controllers.container import SignInContainer
from src.models import SignInModel


class SignInView(View):
    def __init__(self, model: SignInModel):
        super().__init__(
            route=view_enums.Route.SIGN_IN
        )

        self._container = SignInContainer(model)
        self.controls = [
            self._container
        ]
