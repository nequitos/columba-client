
from flet import Page
from flet import (
    RouteChangeEvent,
    ViewPopEvent
)
from flet.app import (
    app_async
)

from src.views import *
from src.static.enums.view import Route


async def main(page: Page):
    page.window.width = 900
    page.window.height = 600

    def route_change(event: RouteChangeEvent):
        page.views.clear()
        page.views.append(
            IndexView()
        )

        if event.route == Route.SIGN_IN:
            page.views.append(SignInView())
        elif event.route == Route.SIGN_UP:
            page.views.append(SignUpView())

        page.update()

    def view_pop(event: ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(Route.INDEX)


if __name__ == "__main__":
    import asyncio

    asyncio.run(
        app_async(
            target=main
        )
    )

