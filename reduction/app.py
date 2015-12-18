from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from reduction import load_ui


class GameWindow(ScreenManager):
    pass


class ReductionApp(App):
    def build(self):
        return GameWindow()

    def run(self):
        load_ui('reduction/ui')
        super(ReductionApp, self).run()
