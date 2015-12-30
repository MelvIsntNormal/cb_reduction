from kivy.uix.widget import Widget

from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.relativelayout import RelativeLayout


class BoardLayout(RelativeLayout):
    cell_size = NumericProperty(85)

    columns = NumericProperty(1)
    rows = NumericProperty(1)
    dimensions = ReferenceListProperty(columns, rows)

    def __init__(self, **kw):
        super(BoardLayout, self).__init__(**kw)
        # Make sure that the board is not resized by it's parent
        self.size_hint = (None, None)

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

        super(BoardLayout, self).do_layout(*largs, **kwargs)

    def _trigger_layout(self, *largs, **kwargs):
        self.do_layout(*largs, **kwargs)

    def pieces_at(self, board_pos):
        print 'Getting pieces at', board_pos
        for child in self.children:
            # I have to explicitly cast both to tuples. I think it's something to do with Kivy properties
            if hasattr(child, 'board_pos') and tuple(child.board_pos) == tuple(board_pos):
                print 'Yielding', child
                yield child

    def coords_to_board_pos(self, pos): return tuple((int(c/self.cell_size) for c in pos))


class BoardPiece(Widget):
    """
    Used to easily add required attributes to elements
    """
    column = NumericProperty(1)
    row = NumericProperty(0)
    board_pos = ReferenceListProperty(column, row)

    def __init__(self, **kwargs):
        super(BoardPiece, self).__init__(**kwargs)

    def on_board_pos(self, piece, board_pos):
        if isinstance(self.parent, BoardLayout):
            print 'Moving piece', piece
            col, row = board_pos
            cell_size = self.parent.cell_size
            self.pos = (
                col * cell_size,
                row * cell_size
            )
