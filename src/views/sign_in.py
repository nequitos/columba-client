
from src.init import session_factory

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
from flet.auth.authorization import OAuth2Token

from src.static.schemes import auth as auth_schemes
from src.static.enums import (
    view as view_enums,
    button as button_enums,
    uri as uri_enums
)



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
        async with session_factory() as session:
            response = await session.post(
                url=uri_enums.Post.SIGN_IN_URI,
                content=auth_schemes.OAuth2(
                    username=self.login_entry.value,
                    password=self.password_entry.value,
                    scopes=["me", "items"]
                ).model_dump_json(),
                headers={
                    "Content-Type": "application/json",
                    "WWW-Authenticate": "Bearer"
                }
            )

            print(response)

    async def on_sign_up(self, event: ControlEvent):
        self.page.go(view_enums.Route.SIGN_UP)

    async def on_back(self, event: ControlEvent):
        self.page.go(view_enums.Route.INDEX)

