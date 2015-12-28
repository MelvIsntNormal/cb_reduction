from kivy.event import EventDispatcher
from kivy.uix.relativelayout import RelativeLayout

from kivy.properties import NumericProperty, ReferenceListProperty, ListProperty, ObjectProperty, BooleanProperty
from kivy.uix.widget import Widget


class Board(RelativeLayout):
    """
    Represents and displays the elements in a level.

    The GridLayout element wasn't used since it had no way of positioning
    elements manually.
    """

    # length of the side of one cell. All cells are square
    cell_size = NumericProperty(85)

    columns = NumericProperty(1)
    rows = NumericProperty(1)
    dimensions = ReferenceListProperty(columns, rows)

    def __init__(self, **kw):
        super(Board, self).__init__(**kw)
        # Make sure that the board is not resized by it's parent
        self.size_hint = (None, None)
        self.player = None

    def load(self, level, player):
        # TODO: find out why I have to do this
        from reduction.component.atom import Atom

        self.player = player

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

    def coords_to_board_pos(self, pos): return tuple((int(c/self.cell_size) for c in pos))

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

    def pieces_at(self, board_pos):
        for child in self.children:
            if hasattr(child, 'board_pos') and tuple(child.board_pos) == board_pos:
                yield child

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


class BoardPiece(Widget):
    """
    Used to easily add required attributes to elements
    """
    column = NumericProperty(1)
    row = NumericProperty(0)
    board_pos = ReferenceListProperty(column, row)

    def __init__(self, **kwargs):
        super(BoardPiece, self).__init__(**kwargs)

    def on_board_pos(self, atom, board_pos):
        if isinstance(self.parent, Board):
            col, row = board_pos
            cell_size = self.parent.cell_size
            self.pos = (
                col * cell_size,
                row * cell_size
            )


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
