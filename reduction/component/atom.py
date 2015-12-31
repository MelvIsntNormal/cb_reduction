from kivy.properties import ListProperty

from kivy.properties import NumericProperty, BooleanProperty

from reduction.component.board_layout import BoardPiece


class Atom(BoardPiece):
    """
    Represents an Atom displayed on the board
    """

    # The core of the atom that determines its element.
    essence = ListProperty([0, 0, 0, 1])

    # Number of ions an atom has, max 8. An atom cannot be operated on without
    # ions
    ions = NumericProperty(1)

    # True if the atom is a target that needs to be met to complete the level
    target = BooleanProperty(False)

    def __init__(self, essence, ions, board_pos, **kwargs):
        self.essence = self.convert_essence(essence)
        self.ions = ions
        self.board_pos = board_pos

        super(Atom, self).__init__(**kwargs)

    @staticmethod
    def convert_essence(essence):
        c, i, e = [0, 0, 0], 0, essence
        while i < 3 and e > 0:
            if e % 2 == 1:
                e -= 1
                c[i] = 1
            e /= 2
            i += 1

        return list(reversed(c)) + [1]

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and not self.target:
            self.parent.player.select(self)
            touch.grab(self)
            return True

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            board_pos = self.parent.coords_to_board_pos(touch.pos)
            if self.parent.can_pass(board_pos):
                self.board_pos = board_pos
            touch.ungrab(self)
            return True

    def on_board_pos(self, piece, board_pos):
        from reduction.component.board import Board

        super(Atom, self).on_board_pos(piece, board_pos)
        if isinstance(self.parent, Board):
            print "Current postition:", self.board_pos
            self.parent.resolve(board_pos)
