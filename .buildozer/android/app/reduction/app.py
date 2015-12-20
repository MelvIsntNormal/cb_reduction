from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager

from reduction import load_ui
from reduction.screen.level import LevelScreen


class GameWindow(ScreenManager):
    pass


class ReductionApp(App):
    def build(self):
        game_window = GameWindow()
        screen = LevelScreen(name='level')
        game_window.add_widget(screen)
        game_window.current_screen = 'level'
        return game_window

    def run(self):
        load_ui('reduction/ui')
        super(ReductionApp, self).run()
