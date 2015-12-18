import os
from kivy.lang import Builder


def get_files(directory, ext=""):
    for root, directories, files in os.walk(directory):
        for filename in files:
            if filename.endswith(ext):
                yield os.path.join(root, filename)


def load_ui(directory):
    for ui_file in get_files(directory, ext=".kv"):
        Builder.load_file(ui_file)
