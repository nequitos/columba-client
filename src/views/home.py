
from uuid import UUID
from typing import Any

from flet import View, Row, Column, Container
from flet import (
    NavigationRail,
    NavigationDrawer,
    NavigationRailDestination,
    NavigationDrawerDestination,
    SearchBar,
    TextField,
    IconButton,
    ListView,
    ElevatedButton,
    CircleAvatar,
    Text,
    FloatingActionButton
)
from flet import Icons, alignment, MainAxisAlignment, NavigationRailLabelType, TextAlign
from flet.core.control_event import ControlEvent

from src.controllers import HomeController
from src.enums import (
    view as view_enums,
    drawer_destination as drawer_destination_enums,
    rail_destination as rail_destination_enums
)


class HomeView(View):
    def __init__(self, controller: HomeController):
        super().__init__(route=view_enums.Route.HOME)

        self.__controller = controller

        self.drawer = NavigationDrawer(
            controls=[
                NavigationDrawerDestination(
                    icon=Icons.SETTINGS_OUTLINED,
                    selected_icon=Icons.SETTINGS,
                    label=drawer_destination_enums.Label.SETTINGS,
                    disabled=True
                ),
                NavigationDrawerDestination(
                    icon=Icons.WALLET_OUTLINED,
                    selected_icon=Icons.WALLET,
                    label=drawer_destination_enums.Label.WALLET,
                    disabled=True
                )
            ]
        )

        self.rail = NavigationRail(
            leading=FloatingActionButton(
                icon=Icons.MANAGE_ACCOUNTS,
                on_click=self.on_manage
            ),
            label_type=NavigationRailLabelType.ALL,
            min_width=80,
            min_extended_width=300,
            group_alignment=-0.9,
            destinations=[
                NavigationRailDestination(
                    icon=Icons.MESSAGE_OUTLINED,
                    selected_icon=Icons.MESSAGE,
                    label=rail_destination_enums.Label.MESSAGES
                ),
                NavigationRailDestination(
                    icon=Icons.GROUP_OUTLINED,
                    selected_icon=Icons.GROUP,
                    label=rail_destination_enums.Label.GROUPS,
                    disabled=True
                ),
                NavigationRailDestination(
                    icon=Icons.LIBRARY_MUSIC_OUTLINED,
                    selected_icon=Icons.LIBRARY_MUSIC,
                    label=rail_destination_enums.Label.MUSIC,
                    disabled=True
                )
            ]
        )

        self.__typesetting_entry: TextField | None = None
        self.__messages_list: ListView | None = None

        self.dialog_container = Container(expand=True)
        self.chats_column = Column(width=250)
        self.controls = [
            self.get_container()
        ]

    def did_mount(self):
        self.page.run_task(self.__controller.set_me_info)
        self.page.run_task(self.update_chats, page=1, size=10)

    async def update_chats(self, page: int, size: int):
        chats = await self.__controller.get_chats(page, size)
        if chats:
            chat_buttons = [
                ElevatedButton(
                    content=Row(
                        [CircleAvatar(), Text(value=f"{chat["username"]}")]
                    ),
                    on_click=self.on_chat,
                    data={
                        "chat_uuid": chat["chat_uuid"],
                        "recipient_uuid": chat["recipient_uuid"]
                    }
                )
                for chat in chats
            ]
            self.chats_column.controls = chat_buttons
            self.page.update()


    def add_message(
        self,
        sender_username: str,
        message_text: str,
        message_account_uuid: UUID,
    ):
        self.__messages_list.controls.append(
            Row(
                [
                    Column(
                        [
                            # Text(sender_username),
                            Text(message_text)
                        ],
                        alignment=MainAxisAlignment.END if self.__controller.uuid == message_account_uuid else MainAxisAlignment.START
                    )
                ],
                expand=True
            )
        )

    def update_dialog_container(
        self, messages: list[dict[str, Any]],
        chat_uuid: UUID,
        recipient_uuid: UUID
    ):
        self.dialog_container.clean()

        if self.__messages_list is not None:
            self.__messages_list.controls.clear()

        column = Column(expand=True)

        self.__messages_list = ListView(expand=True)
        [
            self.add_message(
                sender_username=message["sender_username"],
                message_text=message["text"],
                message_account_uuid=message["account_uuid"]
            )
            for message in messages
        ]
        typesetting_row = self.get_typesetting_row(chat_uuid=chat_uuid)

        column.controls = [
            self.__messages_list,
            typesetting_row
        ]

        self.dialog_container.content = column
        self.page.update()

    def get_container(self) -> Container:
        container = Container(expand=True)
        content_row = Row(
            [
                self.rail,
                self.chats_column,
                self.dialog_container
            ],
            expand=True
        )

        container.content = content_row
        return container


    def get_typesetting_row(self, chat_uuid: UUID) -> Row:
        self.__typesetting_entry = text_field = TextField(expand=True)

        clip_btn = IconButton(
            icon=Icons.ATTACH_FILE_OUTLINED,
            selected_icon=Icons.ATTACH_FILE,
            on_click=self.on_clip
        )
        send_btn = IconButton(
            icon=Icons.SEND_OUTLINED,
            selected_icon=Icons.SEND,
            on_click=self.on_send
        )

        row = Row(
            [
                clip_btn, text_field, send_btn
            ],
            alignment=MainAxisAlignment.CENTER
        )

        return row

    async def on_clip(self, event: ControlEvent) -> None:
        pass

    async def on_manage(self, event: ControlEvent) -> None:
        self.page.open(self.drawer)

    async def on_send(self, event: ControlEvent) -> None:
        message = self.__typesetting_entry.value
        self.__typesetting_entry.clean()

        await self.__controller.send_message(message)
        self.add_message(
            sender_username=self.__controller.username,
            message_text=message,
            message_account_uuid=self.__controller.uuid
        )
        self.page.update()

    async def on_chat(self, event: ControlEvent) -> None:
        chat_uuid = event.control.data["chat_uuid"]
        recipient_uuid = event.control.data["recipient_uuid"]

        messages = await self.__controller.get_chat_messages(1, 20, chat_uuid)
        self.update_dialog_container(messages, chat_uuid, recipient_uuid)
        await self.__controller.open_chat_ws(chat_uuid, recipient_uuid, self.add_message)
