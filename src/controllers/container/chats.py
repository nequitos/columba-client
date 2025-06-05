
from flet import Container, Column, Row
from flet import (
    SearchBar
)
from flet import (
    alignment,
    MainAxisAlignment,
    CrossAxisAlignment
)


from src.models import ChatsModel


class ChatsContainer(Container):
    def __init__(self, model: ChatsModel) -> None:
        super().__init__(
            alignment=alignment.center,
            width=250
        )

        self.search_bar = SearchBar(
            height=40
        )

        self.__model = model
        self._column = Column(
            [
                self.search_bar
            ],
            expand=True
        )

        self.content = self._column

    def did_mount(self):
        self.page.run_task(self.__model.overflow_chats, column=self._column)






