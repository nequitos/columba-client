
from flet import (
    View,
    Container,
    Row,
    Column
)
from flet import (
    NavigationDrawer,
    NavigationDrawerDestination,
    NavigationRailDestination,
    Divider,
    ElevatedButton,
    SearchBar,
    Markdown,
    NavigationRail,
    VerticalDivider,
    FloatingActionButton,
    CircleAvatar,
    IconButton,
    Text,
    TextButton

)
from flet import (
    ControlEvent,
    Icons,
    Icon,
    Colors,
    NavigationRailLabelType,
    MainAxisAlignment,
    alignment
)

from src.static.enums import view as view_enums
from src.init import session


# class DialogContainer(Container):
#     pass
#
#
# class ChatContainer(Container):
#     pass
#
#
# class ProfileContainer(Container):
#     pass



class ChatView(View):
    pass



class HomeView(View):
    def __init__(self):
        super().__init__(
            route=view_enums.Route.HOME
        )

        self.anchor = SearchBar(width=200, height=40)
        self.chat_column = Column(
            # alignment=alignment.top_center,
            controls=[
                self.anchor
            ],
            width=200,
            expand=True
        )

        self.drawer = NavigationDrawer(
            on_change=self.on_drawer_change,
            on_dismiss=self.on_drawer_dismiss,
            controls=[
                NavigationDrawerDestination(
                    icon=Icons.SETTINGS_OUTLINED,
                    selected_icon=Icons.SETTINGS,
                    label="Settings",
                    disabled=True
                ),
                NavigationDrawerDestination(
                    icon=Icons.WALLET_OUTLINED,
                    selected_icon=Icons.WALLET,
                    label="Wallet",
                    disabled=True
                )
            ]
        )

        self.rail = NavigationRail(
            label_type=NavigationRailLabelType.ALL,
            min_width=80,
            min_extended_width=300,
            group_alignment=-0.9,
            on_change=self.on_rail_change,
            leading=FloatingActionButton(
                icon=Icons.MANAGE_ACCOUNTS, on_click=self.on_manage
            ),
            destinations=[
                NavigationRailDestination(
                    icon=Icons.MESSAGE_OUTLINED,
                    selected_icon=Icons.MESSAGE,
                    label="Messages"
                ),
                NavigationRailDestination(
                    icon=Icons.GROUP_OUTLINED,
                    selected_icon=Icons.GROUP,
                    label="Groups",
                    disabled=True
                ),
                NavigationRailDestination(
                    icon=Icons.LIBRARY_MUSIC_OUTLINED,
                    selected_icon=Icons.LIBRARY_MUSIC,
                    label="Music",
                    disabled=True
                )
            ]
        )


        self.controls = [
            Container(
                Row(
                    [
                        self.rail,
                        VerticalDivider(width=1),
                        self.chat_column
                    ]
                ),
                expand=True
            )
        ]

    async def load_chats(self):
        chats = await session.chats()
        print(chats)

        for chat in chats:
            print(chat["first_name"])
            self.chat_column.controls.append(
                Container(
                    TextButton(
                        text=f"{chat["first_name"]} {chat["last_name"]}",
                        # content=Container(CircleAvatar(), alignment=alignment.top_left),
                        width=200,
                    )
                )
            )

    async def on_drawer_change(self, event: ControlEvent):
        match event.data:
            case 0:
                pass

    async def on_drawer_dismiss(self, event: ControlEvent):
        pass

    async def on_rail_change(self, event: ControlEvent):
        match event.data:
            case 0:
                pass
            case 1:
                pass

    async def on_manage(self, event: ControlEvent):
        self.page.open(self.drawer)




