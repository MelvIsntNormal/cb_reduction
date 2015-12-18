from kivy.uix.floatlayout import FloatLayout

from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget


class Board(FloatLayout):
    cell_size = NumericProperty(70)
    columns = NumericProperty(10)
    rows = NumericProperty(5)
    dimensions = ReferenceListProperty(columns, rows)

    def do_layout(self, *largs, **kwargs):
        self.size_hint = (None, None)
        self.size = (self.cell_size * self.columns, self.cell_size * self.rows)
