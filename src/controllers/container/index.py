
from flet import (
    Container,
    ElevatedButton,
    ControlEvent
)
from flet import alignment

from src.models import IndexModel
from src.enums import (
    button as button_enums
)


class IndexContainer(Container):
    def __init__(self, model: IndexModel):
        super().__init__(
            alignment=alignment.center,
            expand=True
        )
        self.__model = model

        self._start_btn = ElevatedButton(
            text=button_enums.Text.START,
            on_click=model.on_start,
            width=250,
            height=50
        )
        self.content = self._start_btn
