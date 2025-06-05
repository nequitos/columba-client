
from flet import (
    Container,
    Row,
    Column
)
from flet import (
    TextField,
    IconButton
)
from flet import (
    Icons,
    alignment,
    MainAxisAlignment
)
from flet.core.list_view import ListView

from src.models import DialogModel


class DialogContainer(Container):
    def __init__(self, model: DialogModel) -> None:
        super().__init__(
            expand=True
        )
        self.__model = model
        self._list_view = ListView(expand=True)
        self._column = Column()

        self.content = Column(
            [
                self._list_view,
                self.get_typesetting_row()
            ]
        )


    def get_typesetting_row(self) -> Row:
        text_field = TextField(expand=True)
        clip_btn = IconButton(
            icon=Icons.ATTACH_FILE_OUTLINED,
            selected_icon=Icons.ATTACH_FILE,
            on_click=self.__model.on_clip_click
        )
        send_btn = IconButton(
            icon=Icons.SEND_OUTLINED,
            selected_icon=Icons.SEND,
            on_click=self.__model.on_send
        )

        row = Row(
            [
                clip_btn, text_field, send_btn
            ],
            alignment=MainAxisAlignment.CENTER
        )

        return row
