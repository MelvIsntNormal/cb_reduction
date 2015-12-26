from kivy.properties import ListProperty

from kivy.properties import NumericProperty, BooleanProperty
from kivy.uix.widget import Widget

from reduction.component.board import BoardPiece


class Atom(Widget, BoardPiece):
    """
    Represents an Atom displayed on the board
    """

    color = ListProperty([1, 0, 0, 0.8])

    # The core of the atom that determines its element.
    essence = NumericProperty(0)

    # Number of ions an atom has, max 8. An atom cannot be operated on without
    # ions
    ions = NumericProperty(1)

    # True if the atom is atarget that needs to be met to complete the level
    target = BooleanProperty(False)

    def __init__(self, essence, ions, board_pos, target, **kwargs):
        self.essence = essence
        self.ions = ions
        self.board_pos = board_pos
        self.target = target

        # Turn a target black
        if self.target:
            self.color[0:2] = [0, 0, 0]
        super(Atom, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.player.select(self)
