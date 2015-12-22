from kivy.properties import ListProperty

from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.widget import Widget

from reduction.component.board import BoardPiece


class Atom(Widget, BoardPiece):
    color = ListProperty([1, 0, 0, 0.8])
    essence = NumericProperty(0)
    ions = NumericProperty(1)
    target = BooleanProperty(False)

    def __init__(self, essence, ions, board_pos, target, **kwargs):
        self.essence = essence
        self.ions = ions
        self.board_pos = board_pos
        self.target = target
        if self.target:
            self.color[0] = 0
        super(Atom, self).__init__(**kwargs)
