

from flet import View

from src.models import EmailCodeModel
from src.controllers.container import EmailCodeContainer
from src.enums import view as view_enums


class EmailCodeView(View):
    def __init__(self, model: EmailCodeModel):
        super().__init__(route=view_enums.Route.EMAIL_CODE)

        self._container = EmailCodeContainer(model)
        self.controls = [
            self._container
        ]

