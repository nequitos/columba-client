
from .base import ModelObject

from flet import Column, Row, ElevatedButton
from flet import (
    CircleAvatar,
    Text,
    Container
)
from flet import (
    MainAxisAlignment,
    alignment,
    TextAlign,
    IconButton,
    CupertinoButton
)



class ChatsModel(ModelObject):
    async def overflow_chats(self, column: Column):
        chat_btn = ElevatedButton(
            on_click=None,
            height=60
        )
        content_text = Text(
            value="Test",
            text_align=TextAlign.START,
            expand=True

        )
        avatar = CircleAvatar(radius=25)

        chat_btn.content = Row([avatar, content_text], alignment=MainAxisAlignment.START)
        column.controls.append(chat_btn)
        self._page.update()