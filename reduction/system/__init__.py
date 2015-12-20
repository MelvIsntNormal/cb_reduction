import os
import yaml
from kivy.lang import Builder

from reduction.system.level import Chapter

chapters = []


def get_files(directory, ext=""):
    for root, directories, files in os.walk(directory):
        for filename in files:
            if filename.endswith(ext):
                yield os.path.join(root, filename)


def load_data(directory=None, test=False):
    for data_file in get_files(directory, '.lvl.yml'):
        data = yaml.load(file(data_file))
        chapters.append(Chapter.from_yaml(data))


def load_ui(directory):
    for ui_file in get_files(directory, ".kv"):
        Builder.load_file(ui_file)


def initialise():
    # load data files
    # load ui files
    load_data('reduction/data/test', True)
    load_ui('reduction/ui')
