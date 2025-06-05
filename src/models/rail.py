
from flet import Page, NavigationDrawer
from flet import ControlEvent


class RailModel:
    def __init__(self, page: Page, drawer: NavigationDrawer) -> None:
        self._page = page
        self._drawer = drawer

    def on_manage(self, event: ControlEvent):
        self._page.open(self._drawer)
