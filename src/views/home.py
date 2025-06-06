
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

    def build(self):
        self.page.run_task(self.__controller.set_me_info)

    def did_mount(self):
        self.page.run_task(self.update_chats)

    async def update_chats(self):
        chats = await self.__controller.get_chats()
        chat_buttons = [
            ElevatedButton(
                content=Row(
                    [CircleAvatar(), Text(f"{chat["first_name"]} {chat["last_name"]}")]
                ),
                on_click=self.on_chat,
                data=chat["uuid"]
            )
            for chat in chats
        ]
        self.chats_column.controls = chat_buttons
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


    def get_typesetting_row(self, send_data: Any) -> Row:
        self.__typesetting_entry = text_field = TextField(expand=True)

        clip_btn = IconButton(
            icon=Icons.ATTACH_FILE_OUTLINED,
            selected_icon=Icons.ATTACH_FILE,
            on_click=self.on_clip
        )
        send_btn = IconButton(
            icon=Icons.SEND_OUTLINED,
            selected_icon=Icons.SEND,
            on_click=self.on_send,
            data=send_data
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

    async def on_send(self, event: ControlEvent) -> None:
        send_response = await self.__controller.send_message(
            text=self.__typesetting_entry.value,
            chat_uuid=event.control.data
        )

        if send_response:
            self.__messages_list.controls.append(
                Row([Text(self.__typesetting_entry.value, text_align=TextAlign.END)], expand=True)
            )
            self.__typesetting_entry.value = ""
            await self.update_chats()
            self.page.update()


    async def on_manage(self, event: ControlEvent) -> None:
        self.page.open(self.drawer)

    async def on_chat(self, event: ControlEvent) -> None:
        chat_content = await self.__controller.get_chat(uuid=event.control.data)
        my_uuid = self.__controller.uuid

        message_rows = [
            Row(
                [
                    Text(
                        f"{message["first_name"]}\n {message["text"]}",
                        text_align=TextAlign.END if my_uuid == message["account_uuid"] else TextAlign.START,
                        expand=True
                    )
                ],
                expand=True
            )
            for message in chat_content["messages"]
        ]

        column = Column()
        self.__messages_list = message_list = ListView(controls=message_rows, expand=True)
        typesetting_row = self.get_typesetting_row(
            send_data=event.control.data
        )

        column.controls = [message_list, typesetting_row]
        self.dialog_container.content = column
        self.page.update()