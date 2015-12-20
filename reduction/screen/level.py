from kivy.uix.screenmanager import Screen


class LevelScreen(Screen):
    def __init__(self, **kw):
        super(LevelScreen, self).__init__(**kw)

    def load_level(self, level):
        self.ids.board.load(level)
