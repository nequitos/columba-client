
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

from src.models import EmailCodeModel
from src.enums import (
    button as button_enums,
    text_field as entry_enums
)


class EmailCodeContainer(Container):
    def __init__(self, model: EmailCodeModel) -> None:
        super().__init__(
            alignment=alignment.center, expand=True
        )
        self.__model = model
        self._code_entry = TextField(
            label=entry_enums.Label.CODE
        )

        self.content = self.get_content_container()

    def get_content_container(self) -> Container:
        column = Column(
            alignment=MainAxisAlignment.CENTER
        )

        confirm_btn = ElevatedButton(
            text=button_enums.Text.CONFIRM,
            on_click=lambda e: self.__model.on_confirm(e, self._code_entry.value),
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
            self._code_entry,
            Row([confirm_btn], alignment=MainAxisAlignment.CENTER),
            Row([back_btn], alignment=MainAxisAlignment.CENTER),
        ]
        content_container = Container(
            alignment=alignment.center,
            content=column,
            width=400,
            expand=True
        )

        return content_container


