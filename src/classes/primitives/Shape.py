from typing import Union, Optional
from collections.abc import Iterable
from ..Stroke import Stroke
from ..Fill import Fill
from ..Item import Item
from ..util.Vector2 import Vector2

class Shape(Item):
    def __init__(self,
            children: Iterable[Item],
            clipped: bool, position: Vector2,
            stroke: Optional[Stroke] = None, fill: Optional[Fill] = None,
            rotation: Union[int, float] = 0
        ):
        super().__init__(rotation)
        for child in children:
            self.add_child(child)
        self.clipped = clipped
        self.position = position
        self.stroke = stroke
        self.fill = fill

    def render(self) -> str:
        raise NotImplementedError
