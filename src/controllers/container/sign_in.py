
from flet import (
    Container,
    Column,
    Row,
    Text,
    TextField,
    ElevatedButton,
    TextButton,
    IconButton
)
from flet import (
    alignment,
    MainAxisAlignment,
    Icons,
    TextCapitalization
)

from src.models import SignInModel
from src.enums import (
    button as button_enums,
    text as text_enums,
    text_field as entry_enums
)

class SignInContainer(Container):
    def __init__(self, model: SignInModel):
        super().__init__(
            alignment=alignment.center,
            expand=True
        )

        self._login_entry = TextField(
            label=entry_enums.Label.LOGIN
        )
        self._password_entry = TextField(
            label=entry_enums.Label.PASSWORD,
            password=True,
            can_reveal_password=True
        )

        self.__model = model
        self.content = Column(
            [
                self.get_entry_column(),
                self.get_button_column()
            ],
            alignment=MainAxisAlignment.CENTER
        )

    def get_entry_column(self) -> Column:
        column = Column(
            width=600,
            alignment=MainAxisAlignment.CENTER,
        )

        column.controls = [
            self._login_entry, self._password_entry
        ]

        return column

    def get_button_column(self) -> Column:
        column = Column(
            width=600,
            alignment=MainAxisAlignment.CENTER
        )

        sign_up_btn = ElevatedButton(
            text=button_enums.Text.SIGN_UP,
            width=100,
            height=40,
            on_click=self.__model.on_sign_up
        )
        sign_in_btn = ElevatedButton(
            text=button_enums.Text.SIGN_IN,
            width=100,
            height=40,
            on_click=self.__model.on_sign_in
        )
        back_btn = ElevatedButton(
            text=button_enums.Text.BACK,
            height=40,
            on_click=self.__model.on_back,
            expand=True
        )

        column.controls = [
            Row(
                [sign_in_btn, sign_up_btn],
                alignment=MainAxisAlignment.END
            ),
            Row(
                [back_btn],
                alignment=MainAxisAlignment.CENTER
            )
        ]

        return column
