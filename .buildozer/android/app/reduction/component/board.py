from kivy.event import EventDispatcher
from kivy.uix.relativelayout import RelativeLayout

from kivy.properties import NumericProperty, ReferenceListProperty, ListProperty
from kivy.uix.widget import Widget


class Board(RelativeLayout):
    cell_size = NumericProperty(80)
    columns = NumericProperty(1)
    rows = NumericProperty(1)
    dimensions = ReferenceListProperty(columns, rows)

    grid = [
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1]
    ]

    def __init__(self, **kw):
        super(Board, self).__init__(**kw)
        self.size_hint = (None, None)
        self.columns = len(self.grid)

        i = 0
        for column in self.grid:
            if self.rows < len(column):
                self.rows = len(column)

            j = 0
            for cell in column:
                print j
                board_pos = (i, j)
                bg_color = []
                if cell == 0:
                    bg_color = [1, 1, 1, 1]
                elif cell == 1:
                    bg_color = [0, 0, 0, 1]

                tile = Tile(board_pos=board_pos, bg_color=bg_color)
                self.add_widget(tile)
                j += 1

            i += 1

        self.size = (self.cell_size * self.columns, self.cell_size * self.rows)

    def do_layout(self, *largs, **kwargs):
        for child in self.children:
            if not hasattr(child, 'board_pos'):
                raise Exception('No board_size attribute')

            col, row = child.board_pos
            child.pos = (
                self.cell_size * col,
                self.cell_size * row
            )

            child.size_hint = (1. / self.columns, 1. / self.rows)

        super(Board, self).do_layout(*largs, **kwargs)


class BoardPiece(EventDispatcher):
    column = NumericProperty(1)
    row = NumericProperty(0)
    board_pos = ReferenceListProperty(column, row)


class Tile(Widget, BoardPiece):
    bg_color = ListProperty([1, 0, 0, 1])
