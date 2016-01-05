from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen

from kivy.properties import StringProperty, NumericProperty, ObjectProperty

from reduction import system
from reduction.system.level import Chapter, Level


class LevelButton(Button):
    _level_select = ObjectProperty(None)
    _chapter = NumericProperty(0)
    _level = StringProperty(None)

    @property
    def chapter(self):
        return system.chapters[self._chapter]

    @property
    def level(self):
        c = self.chapter
        if c is not None and isinstance(c, Chapter):
            return c.levels[self._level]
        else:
            return None

    @property
    def is_locked(self):
        l = self.level
        if l is not None and isinstance(l, Level):
            return not l.is_unlocked
        else:
            return False

    def start_level(self):
        self._level_select.start_level(self._chapter, self._level)


class LevelSelectScreen(Screen):
    def resolve(self):
        self.ids.container.clear_widgets()
        i = 0
        for chapter in system.chapters:
            for lv_id in chapter.levels:
                print lv_id, ": ", chapter.levels[lv_id].is_unlocked
                b = LevelButton(_chapter=i, _level=lv_id, _level_select=self)
                self.ids.container.add_widget(b)
            i += 1

    def start_level(self, ch, lv):
        from reduction.app import GameWindow
        m = self.manager
        if isinstance(m, GameWindow):
            m.load_level(system.chapters[ch].levels[lv], lv)
