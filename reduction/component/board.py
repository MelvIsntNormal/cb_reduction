from kivy.event import EventDispatcher
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout

from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget


class Board(RelativeLayout):
    cell_size = NumericProperty(70)
    columns = NumericProperty(10)
    rows = NumericProperty(5)
    dimensions = ReferenceListProperty(columns, rows)

    def do_layout(self, *largs, **kwargs):
        self.size_hint = (None, None)
        self.size = (self.cell_size * self.columns, self.cell_size * self.rows)

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
    pass
