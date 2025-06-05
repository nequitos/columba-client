
from asyncio import sleep

from flet import (
    Container,
    Column,
    Row
)
from flet import (
    Text,
    TextField,
    ElevatedButton
)
from flet import (
    alignment,
    MainAxisAlignment,
    ControlEvent
)

from src.models import SignUpModel
from src.enums import (
    button as button_enums,
    text as text_enums,
    text_field as entry_enums
)


class SignUpContainer(Container):
    def __init__(self, model: SignUpModel) -> None:
        super().__init__(
            alignment=alignment.center, expand=True
        )
        self.__model = model
        self._email_entry = TextField(
            label=entry_enums.Label.EMAIL
        )

        self.content = self.get_content_container()

    def get_content_container(self) -> Container:
        column = Column(
            alignment=MainAxisAlignment.CENTER
        )

        send_code_btn = ElevatedButton(
            text=button_enums.Text.CONTINUE,
            on_click=lambda e: self.__model.on_send_code(e, self._email_entry.value),
            height=40,
            expand=True
        )
        back_btn = ElevatedButton(
            text=button_enums.Text.BACK,
            on_click=self.__model.on_back,
            height=40,
            expand=True
        )

        column.controls = [
            self._email_entry,
            Row([send_code_btn], alignment=MainAxisAlignment.CENTER),
            Row([back_btn], alignment=MainAxisAlignment.CENTER),
        ]
        content_container = Container(
            alignment=alignment.center,
            content=column,
            width=400,
            expand=True
        )

        return content_container



