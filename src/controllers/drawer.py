
from flet import (
    NavigationDrawer,
    NavigationDrawerDestination
)
from flet import Icons, ControlEvent

from src.enums import (
    drawer_destination as drawer_destination_enums
)


class Drawer(NavigationDrawer):
    def __init__(self):
        super().__init__()

        self.controls = [
            NavigationDrawerDestination(
                icon=Icons.SETTINGS_OUTLINED,
                selected_icon=Icons.SETTINGS,
                label=drawer_destination_enums.Label.SETTINGS,
                disabled=True
            ),
            NavigationDrawerDestination(
                icon=Icons.WALLET_OUTLINED,
                selected_icon=Icons.WALLET,
                label=drawer_destination_enums.Label.WALLET,
                disabled=True
            )
        ]