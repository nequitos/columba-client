
from flet import (
    View
)

from src.static.enums import view as view_enums


class HomeView(View):
    def __init__(self):
        super().__init__(
            route=view_enums.Route.HOME
        )

