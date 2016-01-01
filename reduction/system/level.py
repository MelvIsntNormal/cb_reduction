"""
Classes here are simply data structures
"""


class Chapter:
    def __init__(self, _id, _title, _levels):
        self.title = _title
        self.levels = _levels

    @classmethod
    def from_yaml(cls,  data):
        id = data['id']
        title = data['title']
        levels = {}
        for key, level in data['levels'].iteritems():
            levels[key] = Level.from_yaml(level)
        return cls(id, title, levels)


class Level:
    def __init__(self, title, energy, world, **kwargs):
        self.title = title
        self.energy = energy
        self.world = world

    @classmethod
    def from_yaml(cls, data):
        return cls(**data)


