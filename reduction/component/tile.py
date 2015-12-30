from kivy.properties import ListProperty, BooleanProperty

from reduction.component.board_layout import BoardPiece


class Tile(BoardPiece):
    """
    Represents cells in grid
    """
    bg_color = ListProperty([1, 0, 0, 1])
    passable = BooleanProperty(True)

    def __init__(self, **kwargs):
        self.on_passable()
        super(Tile, self).__init__(**kwargs)

    def on_passable(self, *largs, **kwargs):
        self.bg_color = ([1, 1, 1] if self.passable else [0, 0, 0]) + [1]


class TargetTile(BoardPiece):
    pass
