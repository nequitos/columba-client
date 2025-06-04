
from httpx import BasicAuth

from flet import (
    View,
    Container,
    Row,
    Column
)
from flet import (
    Text,
    TextField,
    ElevatedButton
)
from flet import (
    ControlEvent
)
from flet import alignment, MainAxisAlignment

from src.static.enums import (
    view as view_enums,
    button as button_enums
)
from src.init import session, oath2


class SignInView(View):
    def __init__(self):
        super().__init__(
            route=view_enums.Route.SIGN_IN
        )

        self.login_entry = TextField(expand=True)
        self.password_entry = TextField(expand=True)

        self.controls = [
            Container(
                Column(
                    [
                        Row(
                            [
                                Text(value="Login:", width=100),
                                self.login_entry
                            ],
                            alignment=MainAxisAlignment.START
                        ),
                        Row(
                            [
                                Text(value="Password:", width=100),
                                self.password_entry
                            ],
                            alignment=MainAxisAlignment.START,
                        ),
                        Row(
                            [
                                ElevatedButton(
                                    text=button_enums.Text.SIGN_UP,
                                    width=100,
                                    height=40,
                                    on_click=self.on_sign_up
                                ),
                                ElevatedButton(
                                    text=button_enums.Text.SIGN_IN,
                                    width=100,
                                    height=40,
                                    on_click=self.on_sign_in
                                )
                            ],
                            alignment=MainAxisAlignment.END
                        ),
                        Row(
                            [
                                ElevatedButton(
                                    text=button_enums.Text.BACK,
                                    height=40,
                                    on_click=self.on_back,
                                    expand=True
                                )
                            ],
                            alignment=MainAxisAlignment.CENTER
                        )
                    ],
                    width=600,
                    alignment=MainAxisAlignment.CENTER
                ),
                expand=True,
                alignment=alignment.center
            )
        ]

    async def on_sign_in(self, event: ControlEvent):
        oath2.set_credentials(
            username=self.login_entry.value,
            password=self.password_entry.value
        )
        if await oath2.authorize_account():
            self.page.go(view_enums.Route.HOME)

    async def on_sign_up(self, event: ControlEvent):
        self.page.go(view_enums.Route.SIGN_UP)

    async def on_back(self, event: ControlEvent):
        self.page.go(view_enums.Route.INDEX)

