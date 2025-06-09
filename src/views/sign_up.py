

from flet import View, Row, Column
from flet import (
    Container,
    TextField,
    ElevatedButton
)
from flet import ControlEvent
from flet import alignment, MainAxisAlignment

from src.controllers import SignUpController

from src.session.schemes import auth as auth_schemes
from src.enums import (
    view as view_enums,
    button as button_enums,
    text_field as text_field_enums
)


class SignUpView(View):
    def __init__(
        self,
        controller: SignUpController
    ) -> None:
        super().__init__(route=view_enums.Route.SIGN_UP)

        self.__controller = controller

        self.email_entry = TextField(
            label=text_field_enums.Label.EMAIL,
            expand=True
        )
        self.username_entry = TextField(
            label=text_field_enums.Label.USERNAME,
            expand=True
        )
        self.pwd_entry = TextField(
            label=text_field_enums.Label.PASSWORD,
            expand=True
        )
        self.re_pwd_entry = TextField(
            label=text_field_enums.Label.RE_PWD,
            expand=True
        )
        self.code_entry = TextField(
            label=text_field_enums.Label.CODE,
            expand=True
        )

        self.send_code_btn = ElevatedButton(
            text=button_enums.Text.SEND_CODE,
            expand=True,
            on_click=self.on_send_code
        )
        self.confirm_btn = ElevatedButton(
            text=button_enums.Text.CONFIRM,
            expand=True,
            on_click=self.on_confirm
        )
        self.back_btn = ElevatedButton(
            text=button_enums.Text.BACK,
            expand=True,
            on_click=self.on_back
        )

        self.controls = [
            self.get_first_container()
        ]

    def get_first_container(self) -> Container:
        container = Container(
            alignment=alignment.center,
            expand=True
        )

        content_column = Column(
            [
                Row([self.email_entry]),
                Row([self.send_code_btn]),
                Row([self.back_btn])
            ],
            expand=True,
            width=400,
            alignment=MainAxisAlignment.CENTER
        )
        container.content = content_column

        return container

    def get_second_container(self) -> Container:
        self.controls.clear()

        container = Container(
            alignment=alignment.center,
            expand=True
        )

        content_column = Column(
            [
                Row([self.username_entry]),
                Row([self.pwd_entry]),
                Row([self.re_pwd_entry]),
                Row([self.code_entry]),
                Row([self.confirm_btn]),
                Row([self.back_btn])
            ],
            expand=True,
            width=400,
            alignment=MainAxisAlignment.CENTER
        )
        container.content = content_column
        return container

    async def on_send_code(self, event: ControlEvent):
        if await self.__controller.on_sign_up(email=self.email_entry.value):
            container = self.get_second_container()
            self.controls = [container]
            self.page.update()
        else:
            pass

    async def on_confirm(self, event: ControlEvent):
        if self.pwd_entry.value == self.re_pwd_entry.value:
            if await self.__controller.verify_code(
                email=self.email_entry.value,
                username=self.username_entry.value,
                code=self.code_entry.value,
                password=self.pwd_entry.value
            ):
                self.page.go(view_enums.Route.HOME)


    async def on_back(self, event: ControlEvent) -> None:
        self.page.go(view_enums.Route.SIGN_IN)