from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class GameWindow(FloatLayout):
    pass


class ReductionApp(App):
    def build(self):
        return GameWindow()
