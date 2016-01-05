from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import Screen

from kivy.properties import StringProperty, ObjectProperty

from reduction.system.save_data import level_complete


class LevelScreen(Screen):
    """
    A screen used to display actual gameplay
    """

    _current_level_id = StringProperty(None)

    def __init__(self, **kw):
        super(LevelScreen, self).__init__(**kw)

    def load_level(self, level, lv_id):
        self._current_level_id = lv_id
        self.ids.player.load(level)
        self.ids.board.load(level, self.ids.player)

    def process_win(self):
        print self._current_level_id
        level_complete(self._current_level_id)
        view = LevelCompleteModal(self)
        view.open()


class LevelCompleteModal(ModalView):
    screen = ObjectProperty(None)

    def __init__(self ,screen, **kwargs):
        super(LevelCompleteModal, self).__init__(**kwargs)
        self.screen = screen

    def load_level_select(self):
        s = self.screen
        if isinstance(s, LevelScreen):
            print 'Loading...'
            self.dismiss()
            s.manager.load_level_select()
        else:
            print "Something's wrong... ", s

