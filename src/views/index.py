
from flet import (
    View,
    Container,
    ElevatedButton,
    ControlEvent
)
from flet import alignment

from src.enums import (
    view as view_enums,
    button as button_enums
)


class IndexView(View):
    def __init__(self):
        super().__init__(route=view_enums.Route.INDEX)

        self.start_btn = ElevatedButton(
            text=button_enums.Text.START,
            width=250,
            height=50,
            on_click=self.on_start
        )

        self.controls = [
            self.get_container()
        ]

    def get_container(self) -> Container:
        container = Container(expand=True, alignment=alignment.center)

        container.content = self.start_btn
        return container

    async def on_start(self, event: ControlEvent):
        self.page.go(view_enums.Route.SIGN_IN)

