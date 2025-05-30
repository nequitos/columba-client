
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
from flet import (
    MainAxisAlignment,
    alignment
)

from src.static.enums import (
    button as button_enums,
    label as label_enums,
    view as view_enums
)
from src.client.schemes.auth import CreateAccount
from src.init import session, URI


class SignUpView(View):
    def __init__(self):
        super().__init__(
            route=view_enums.Route.SIGN_UP
        )

        self.first_name_entry = TextField(expand=True)
        self.last_name_entry = TextField(expand=True)
        self.email_entry = TextField(expand=True)
        self.password_entry = TextField(expand=True)
        self.retype_password_entry = TextField(expand=True)

        self.controls = [
            Container(
                Column(
                    [
                        Row(
                            [
                                Text(value=label_enums.Value.FIRST_NAME, width=100),
                                self.first_name_entry
                            ]
                        ),
                        Row(
                            [
                                Text(value=label_enums.Value.LAST_NAME, width=100),
                                self.last_name_entry
                            ]
                        ),
                        Row(
                            [
                                Text(value=label_enums.Value.EMAIL, width=100),
                                self.email_entry
                            ]
                        ),
                        Row(
                            [
                                Text(value=label_enums.Value.PASSWORD, width=100),
                                self.password_entry
                            ],
                        ),
                        Row(
                            [
                                Text(value=label_enums.Value.RETYPE_PASSWORD, width=100),
                                self.retype_password_entry
                            ]
                        ),
                        Row(
                            [
                                ElevatedButton(
                                    text=button_enums.Text.CONFIRM,
                                    on_click=self.on_sing_up,
                                    width=100,
                                    height=40,
                                    expand=True
                                )
                            ]
                        ),
                        Row(
                            [
                                ElevatedButton(
                                    text=button_enums.Text.BACK,
                                    on_click=self.on_back,
                                    width=100,
                                    height=40,
                                    expand=True
                                )
                            ]
                        )
                    ],
                    width=600,
                    alignment=MainAxisAlignment.CENTER
                ),
                expand=True,
                alignment=alignment.center
            )
        ]


    async def on_back(self, event: ControlEvent) -> None:
        self.page.go(view_enums.Route.SIGN_IN)

    async def on_sing_up(self, event: ControlEvent) -> None:
        if (
            self.password_entry.value == self.retype_password_entry.value and
            self.first_name_entry is not None and
            self.last_name_entry is not None
        ):
            await session.post(
                URI.ACCOUNT_CREATE_URI.value,
                CreateAccount(
                    first_name=self.first_name_entry.value,
                    last_name=self.last_name_entry.value,
                    password=self.password_entry.value,
                    email=self.email_entry.value
                ).model_dump()
            )