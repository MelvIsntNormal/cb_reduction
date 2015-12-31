from kivy.app import App
from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.screenmanager import ScreenManager

from reduction import system
from reduction.screen.level import LevelScreen


class GameWindow(ScreenManager):
    pass


class ReductionApp(App):

    def build(self):
        game_window = GameWindow()
        screen = LevelScreen(name='level')
        game_window.add_widget(screen)
        screen.load_level(system.chapters[0].levels['test_world'])
        game_window.current_screen = 'level'
        return game_window

    def run(self):
        system.initialise()
        super(ReductionApp, self).run()
