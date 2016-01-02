from kivy.properties import ListProperty, BooleanProperty, NumericProperty

from reduction.component.atom import Atom
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


class VoidTile(BoardPiece):
    essence = ListProperty([0, 0, 0, 1])
    ions = NumericProperty(1)

    def __init__(self, essence, ions, board_pos, *largs, **kwargs):
        super(VoidTile, self).__init__(*largs, **kwargs)
        self.essence = Atom.convert_essence(essence)
        self.ions = ions
        self.board_pos = board_pos

    def can_be_completed_by(self, atom):
        if not isinstance(atom, Atom):
            raise ValueError("Only Atoms can complete Voids")

        return atom.essence == self.essence and atom.ions == self.ions

    @property
    def is_complete(self):
        from reduction.component.board import Board
        board = self.parent
        if isinstance(board, Board):
            atoms = filter(lambda x: isinstance(x, Atom), board.pieces_at(self.board_pos))
            if len(atoms) > 0 and self.can_be_completed_by(atoms[0]):
                return True
        return False

