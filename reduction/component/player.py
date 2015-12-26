from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

from reduction.component.board import BoardPiece


class Player(Widget):
    """
    Handles selection of board pieces.

    Player can only select one element at a time
    """

    selected = ObjectProperty(Widget(size=(0, 0)))

    def load(self, level):
        self.selected = Widget(size=(0, 0))

    def select(self, piece):
        print piece
        self.selected = piece
        self.size = piece.size
        self.pos = piece.pos
