
from flet import (
    Container,
    Row,
    Column,
    VerticalDivider,
    SearchBar,
    Text,
    TextAlign,
    ListView,
    Dismissible
)
from flet import (
    MainAxisAlignment,
    CrossAxisAlignment,
    alignment
)

from .dialog import DialogContainer
from .chats import ChatsContainer

from src.models import HomeModel, DialogModel, ChatsModel
from src.controllers.rail import Rail


class HomeContainer(Container):
    def __init__(
        self,
        home_model: HomeModel,
        dialog_model: DialogModel,
        chats_model: ChatsModel,
        rail: Rail,
    ) -> None:
        super().__init__(
            expand=True,
            alignment=alignment.center
        )
        self._rail = rail
        self.__home_model = home_model
        self.__dialog_model = dialog_model
        self.__chats_model = chats_model

        self._dialog_container = DialogContainer(dialog_model)
        self._chats_container = ChatsContainer(chats_model)

        self.content = Row(
            [
                self.get_nav_row(),
                VerticalDivider(width=1),
                self._chats_container,
                VerticalDivider(width=1),
                self._dialog_container
            ],
            alignment=MainAxisAlignment.START,
            expand=True
        )

    def get_nav_row(self) -> Row:
        row = Row(
            [self._rail],
            alignment=MainAxisAlignment.START,
        )

        return row
