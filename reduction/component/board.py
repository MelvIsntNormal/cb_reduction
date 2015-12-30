from kivy.properties import NumericProperty, ReferenceListProperty, ListProperty, ObjectProperty, BooleanProperty

from reduction.component.board_layout import BoardPiece, BoardLayout


class Board(BoardLayout):
    """
    Represents and displays the elements in a level.

    The GridLayout element wasn't used since it had no way of positioning
    elements manually.
    """

    def __init__(self, **kw):
        super(Board, self).__init__(**kw)

    def load(self, level, player):
        # TODO: find out why I have to do this
        from reduction.component.atom import Atom

        # small alias for the world as I used grid in testing code
        # Should probably refactor
        grid = level.world
        self.columns = len(grid)

        # iterate through grid while keeping cell reference
        i = 0
        for column in grid:
            # attempt to adjust dimensions to greatest column length
            if self.rows < len(column):
                self.rows = len(column)

            j = 0
            for cell in column:
                board_pos = (i, j)
                passable = True if cell == 0 else False

                tile = Tile(board_pos=board_pos, passable=passable)
                self.add_widget(tile)
                j += 1

            i += 1

        self.size = (self.cell_size * self.columns, self.cell_size * self.rows)

        for atom in level.atoms:
            # destruct an array as positional arguments for constructor
            a = Atom(*atom)
            self.add_widget(a)

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
        print 'Resolving position', board_pos
        atoms = filter(lambda a: isinstance(a, Atom), self.pieces_at(board_pos))
        target = filter(lambda a: a.target, atoms)


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
