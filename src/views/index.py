
from flet import View

from src.enums import view as view_enums
from src.models import IndexModel

from src.controllers.container import IndexContainer


class IndexView(View):
    def __init__(self, model: IndexModel) -> None:
        super().__init__(
            route=view_enums.Route.INDEX
        )

        self._container = IndexContainer(model)
        self.controls = [self._container]