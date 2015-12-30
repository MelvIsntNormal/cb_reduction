from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

from reduction.component.board import BoardPiece, Board, Tile
from reduction.component.board_layout import BoardLayout


class Selector(BoardPiece):
    selected = ObjectProperty()

    def select(self, piece):
        if isinstance(piece, BoardPiece):
            self.selected = piece
            self.board_pos = piece.board_pos
            self.size = piece.size


class Targetor(BoardPiece):
    pass


class Player(BoardLayout):
    """
    Handles selection of board pieces.

    Player can only select one element at a time
    """

    selector = ObjectProperty(Selector(id='selector'))
    targetor = ObjectProperty(Targetor(id='targetor'))
    board = ObjectProperty(None)

    def __init__(self, *largs, **kwargs):
        super(Player, self).__init__(*largs, **kwargs)
        self.add_widget(self.selector)

    def do_layout(self, *largs, **kwargs):
        super(Player, self).do_layout(*largs, **kwargs)

    def load(self, level):
        self.do_layout()
        self.select((Tile(size=(0, 0), board_pos=(-1, -1))))

    def select(self, piece):
        self.selector.select(piece)
