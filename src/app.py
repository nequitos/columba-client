
from flet import (
    app_async,
    PagePlatform,
    Page,
    AppView,
    ViewPopEvent,
    RouteChangeEvent
)


from src.enums import view as view_enums
# from src.controllers.drawer import Drawer
# from src.controllers.rail import Rail

from session import BaseSession, OAuth2
from src.views.home import HomeView
from views import *
from models import *
from controllers import *


oauth = OAuth2("http", "localhost", 8000, "/oauth/v2/token")
session = BaseSession("http", "localhost", 8000, oauth)


# --- Models initialize --- #
sign_in_model = SignInModel()
sign_up_model = SignUpModel()
home_model = HomeModel()

# --- Controllers initialize --- #
sign_in_controller = SingInController(model=sign_in_model, oauth=oauth)
sign_up_controller = SignUpController(model=sign_up_model, session=session, oauth=oauth)
home_controller = HomeController(model=home_model, session=session)


class App:
    def __init__(
        self, page: Page
    ) -> None:
        self._page = _page = page

        # self._drawer = drawer = Drawer()
        # self._rail = Rail(RailModel(page, drawer))

        page.on_view_pop = self._view_pop_cb
        page.on_route_change = self._route_change_cb

        self.__preload_size()
        page.go(view_enums.Route.INDEX)

    def __preload_size(self):
        pass
        self._page.window.width = 900
        self._page.window.height = 600
        # self._page.window.max_width = 900
        # self._page.window.max_height = 600
        self._page.window.min_width = 900
        self._page.window.min_height = 400

    def _view_pop_cb(self, event: ViewPopEvent) -> None:
        self._page.views.pop()
        top_view = self._page.views[-1]
        self._page.go(top_view.route)

    def _route_change_cb(self, event: RouteChangeEvent) -> None:
        views = self._page.views
        views.clear()
        views.append(
            IndexView()
        )

        if event.route == view_enums.Route.SIGN_IN:
            views.append(SignInView(sign_in_controller))
        elif event.route == view_enums.Route.SIGN_UP:
            views.append(SignUpView(sign_up_controller))
        elif event.route == view_enums.Route.HOME:
            views.append(HomeView(home_controller))

        self._page.update()


if __name__ == "__main__":
    import asyncio

    asyncio.run(
        app_async(
            target=App,
            view=AppView.FLET_APP_WEB
        )
    )
