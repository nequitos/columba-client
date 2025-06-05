
from flet import (
    NavigationRail,
    FloatingActionButton,
    NavigationRailDestination,
    NavigationDrawer
)
from flet import (
    Icons,
    NavigationRailLabelType,
    ControlEvent
)

from src.models import RailModel
from src.enums import (
    rail_destination as rail_destination_enums
)


class Rail(NavigationRail):
    def __init__(self, model: RailModel):
        super().__init__(
            leading=FloatingActionButton(
                icon=Icons.MANAGE_ACCOUNTS,
                on_click=model.on_manage
            ),
            label_type=NavigationRailLabelType.ALL,
            min_width=80,
            min_extended_width=300,
            group_alignment=-0.9,
        )
        self.__model = model

        self.destinations = [
            NavigationRailDestination(
                icon=Icons.MESSAGE_OUTLINED,
                selected_icon=Icons.MESSAGE,
                label=rail_destination_enums.Label.MESSAGES
            ),
            NavigationRailDestination(
                icon=Icons.GROUP_OUTLINED,
                selected_icon=Icons.GROUP,
                label=rail_destination_enums.Label.GROUPS,
                disabled=True
            ),
            NavigationRailDestination(
                icon=Icons.LIBRARY_MUSIC_OUTLINED,
                selected_icon=Icons.LIBRARY_MUSIC,
                label=rail_destination_enums.Label.MUSIC,
                disabled=True
            )
        ]

    # @property
    # def manage_drawer(self) -> NavigationDrawer:
    #     return self.page.drawer
    #
    # async def change(self, event: ControlEvent):
    #     pass
