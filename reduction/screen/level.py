from kivy.uix.screenmanager import Screen


class LevelScreen(Screen):
    """
    A screen used to display actual gameplay
    """

    def __init__(self, **kw):
        super(LevelScreen, self).__init__(**kw)

    def load_level(self, level):
        self.ids.player.load(level)
        self.ids.board.load(level, self.ids.player)
