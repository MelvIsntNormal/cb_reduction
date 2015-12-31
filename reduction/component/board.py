from reduction.component.board_layout import BoardLayout
from reduction.component.tile import Tile, VoidTile


class Board(BoardLayout):
    """
    Represents and displays the elements in a level.

    The GridLayout element wasn't used since it had no way of positioning
    elements manually.


    Notes:
        - Constraints:
          - Each cell can only be occupied by one Tile
          - Each cell can only be occupied by one Atom, or two atoms that can immediately reduce
        - A level is completed when all voids (targets) have been filled with the correct atom
    """

    def __init__(self, **kw):
        super(Board, self).__init__(**kw)

    def load(self, level, player):
        self.columns = len(level.world['tiles'])
        self.rows = 0
        for column in level.world['tiles']:
            if self.rows < len(column):
                self.rows = len(column)

        self.size = (self.cell_size * self.columns, self.cell_size * self.rows)

        for widget in self.build_children(**level.world):
            self.add_widget(widget)

    @staticmethod
    def build_children(tiles, voids, atoms):
        from reduction.component.atom import Atom

        i = 0
        for column in tiles:
            j = 0
            for cell in column:
                board_pos = (i, j)
                passable = True if cell == 0 else False

                yield Tile(board_pos=board_pos, passable=passable)
                j += 1

            i += 1

        for void in voids:
            yield VoidTile(*void)

        for atom in atoms:
            # destruct an array as positional arguments for constructor
            yield Atom(*atom)

    def do_layout(self, *largs, **kwargs):
        for child in self.children:
            # All children must have this attribute
            if not hasattr(child, 'board_pos'):
                raise Exception('No board_size attribute')

            # col <- x dimension, row <- y dimension
            col, row = child.board_pos
            child.pos = (
                self.cell_size * col,
                self.cell_size * row
            )

            # resize all children to fit in one cell
            # will adjust to allow for scaling
            child.size_hint = (1. / self.columns, 1. / self.rows)

        super(Board, self).do_layout(*largs, **kwargs)

    def can_pass(self, board_pos):
        # check that position is within grid boundaries
        if 0 <= board_pos[0] <= self.columns or 0 <= board_pos[1] <= self.rows:
            # For each piece that occupies that position
            for piece in self.pieces_at(board_pos):
                # If it can be inhabited, return True
                if isinstance(piece, Tile) and piece.passable:
                    return True
        # position can't be inhabited or is our of bounds
        return False

    def resolve(self, board_pos):
        from reduction.component.atom import Atom

        # Each cell on the Board can only be inhabited by one atom at any given time
        # If there are two atoms in the same space, they must reduce to one

        print 'Resolving position', board_pos
        atoms = filter(lambda a: isinstance(a, Atom), self.pieces_at(board_pos))
        target = filter(lambda a: a.target, atoms)

