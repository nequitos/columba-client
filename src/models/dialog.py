
from .base import ModelObject

from flet import ControlEvent


class DialogModel(ModelObject):
    def on_clip_click(self, event: ControlEvent) -> None:
        pass

    async def on_send(self, event: ControlEvent) -> None:
        pass