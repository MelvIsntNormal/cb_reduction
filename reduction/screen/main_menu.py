from kivy.uix.screenmanager import Screen


class MainMenuScreen(Screen):
    def load_select_screen(self, *largs, **kwargs):
        from reduction.app import GameWindow
        m = self.manager
        if isinstance(m, GameWindow):
            m.load_level_select()
