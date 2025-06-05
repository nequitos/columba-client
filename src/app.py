
from flet import (
    app_async,
    PagePlatform,
    Page,
    AppView,
    ViewPopEvent,
    RouteChangeEvent
)


from src.enums import view as view_enums
from src.controllers.drawer import Drawer
from src.controllers.rail import Rail

from views import *
from models import *


class App:
    def __init__(
        self, page: Page
    ) -> None:
        self._page = _page = page

        self._drawer = drawer = Drawer()
        self._rail = Rail(RailModel(page, drawer))

        self.sign_in_model = SignInModel(page)
        self.sign_up_model = SignInModel(page)
        self.email_code_model = EmailCodeModel(page)
        self.home_model = EmailCodeModel(page)
        self.chats_model = ChatsModel(page)
        self.dialog_model = DialogModel(page)

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
            IndexView(IndexModel(self._page))
        )

        if event.route == view_enums.Route.SIGN_IN:
            views.append(SignInView(self.sign_in_model))
        elif event.route == view_enums.Route.SIGN_UP:
            views.append(SignUpView(self.sign_up_model))
        elif event.route == view_enums.Route.EMAIL_CODE:
            views.append(EmailCodeView(self.email_code_model))
        elif event.route == view_enums.Route.HOME:
            home_view = HomeView(
                chats_model=self.chats_model,
                dialog_model=self.dialog_model,
                home_model=self.home_model,
                drawer=self._drawer,
                rail=self._rail
            )
            views.append(home_view)

        self._page.update()



if __name__ == "__main__":
    import asyncio

    asyncio.run(
        app_async(
            target=App,
            view=AppView.FLET_APP_WEB
        )
    )
