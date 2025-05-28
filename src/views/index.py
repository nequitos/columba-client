
from flet import (
    View,
    Container,
    Row
)
from flet import ElevatedButton
from flet import ControlEvent
from flet import alignment
from flet.core.types import MainAxisAlignment

from src.static.enums import (
    button as button_enums,
    view as view_enums
)



class IndexView(View):
    def __init__(self):
        super().__init__(
            route=view_enums.Route.INDEX
        )

        self.controls = [
            Container(
                ElevatedButton(
                    text=button_enums.Text.START,
                    on_click=self.on_sign_in,
                    width=250,
                    height=50
                ),
                alignment=alignment.center,
                expand=True
            )
        ]

    async def on_sign_in(self, event: ControlEvent):
        self.page.go(view_enums.Route.SIGN_IN)