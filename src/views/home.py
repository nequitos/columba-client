
from flet import View, Container, Row
from flet.core.column import Column

from src.enums import (
    view as view_enums
)

from src.models import HomeModel, DialogModel, ChatsModel
from src.controllers.container import (
    HomeContainer,
    DialogContainer
)
from src.controllers.rail import Rail
from src.controllers.drawer import Drawer


class HomeView(View):
    def __init__(
        self,
        chats_model: ChatsModel,
        home_model: HomeModel,
        dialog_model: DialogModel,
        drawer: Drawer,
        rail: Rail
    ) -> None:
        super().__init__(
            route=view_enums.Route.HOME
        )
        self._container = HomeContainer(
            chats_model=chats_model,
            home_model=home_model,
            dialog_model=dialog_model,
            rail=rail
        )
        self.drawer = drawer

        self.controls = [
            self._container
        ]