from kivy.app import App
from kivy.core.window import Window
from kivy.modules import inspector
from kivy.uix.screenmanager import ScreenManager

from reduction import system
from reduction.screen.level import LevelScreen
from reduction.screen.level_select import LevelSelectScreen
from reduction.screen.main_menu import MainMenuScreen


class GameWindow(ScreenManager):
    def __init__(self, *largs, **kwargs):
        super(GameWindow, self).__init__(*largs, **kwargs)
        self._main = MainMenuScreen(name='main_menu')
        self._level_select = LevelSelectScreen(name='level_select')
        self._level = LevelScreen(name='level')

    def _load(self, screen):
        if screen not in self.screens:
            self.add_widget(screen)
        self.current = screen.name

    def load_level(self, level, lv_id):
        self._level.load_level(level, lv_id)
        self._load(self._level)

    def load_main_menu(self):
        self._load(self._main)

    def load_level_select(self):
        self._level_select.resolve()
        self._load(self._level_select)


class ReductionApp(App):

    def build(self):
        game_window = GameWindow()
        # game_window.load_level(system.chapters[0].levels['reduction'])
        game_window.load_main_menu()
        return game_window

    def run(self):
        system.initialise()
        super(ReductionApp, self).run()
