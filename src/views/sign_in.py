
from flet import (
    View,
    Row,
    Column,
    Container
)
from flet import (
    TextField,
    ElevatedButton
)
from flet import (
    ControlEvent
)
from flet import alignment, MainAxisAlignment


from src.session.schemes import auth as auth_schemes
from src.controllers import SingInController
from src.enums import (
    view as view_enums,
    text_field as text_field_enums,
    button as button_enum
)


class SignInView(View):
    def __init__(
        self,
        controller: SingInController
    ) -> None:
        super().__init__(route=view_enums.Route.SIGN_IN)

        self.__controller = controller

        self.sign_in_btn = ElevatedButton(
            text=button_enum.Text.SIGN_IN,
            on_click=self.on_sign_in,
            expand=True
        )
        self.sign_up_btn = ElevatedButton(
            text=button_enum.Text.SIGN_UP,
            on_click=self.on_sign_up,
            expand=True
        )

        self.login_entry = TextField(
            label=text_field_enums.Label.LOGIN,
            expand=True
        )
        self.pwd_entry = TextField(
            label=text_field_enums.Label.PASSWORD,
            password=True,
            can_reveal_password=True,
            expand=True
        )

        self.controls = [
            self.get_container()
        ]

    def get_container(self):
        container = Container(
            alignment=alignment.center,
            expand=True
        )

        content_column = Column(
            [
                Row([self.login_entry]),
                Row([self.pwd_entry]),
                Row([self.sign_in_btn]),
                Row([self.sign_up_btn])
            ],
            expand=True,
            width=400,
            alignment=MainAxisAlignment.CENTER
        )
        container.content = content_column

        return container

    async def on_sign_in(self, event: ControlEvent):
        scheme = auth_schemes.AuthRequest(
            username=self.login_entry.value,
            password=self.pwd_entry.value
        )
        if await self.__controller.on_sign_in(scheme):
            self.page.go(view_enums.Route.HOME)

    async def on_sign_up(self, event: ControlEvent):
        self.page.go(view_enums.Route.SIGN_UP)