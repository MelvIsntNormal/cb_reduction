"""
Classes here are simply data structures
"""
from reduction.system import save_data


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
    def __init__(self, title, requirements, energy, world, **kwargs):
        self.title = title
        self.requirements = requirements
        self.energy = energy
        self.world = world

        print self.is_unlocked

    @property
    def is_unlocked(self):
        return self.requirements is None or all([
            self.requirements['succeeds'] is None or self.requirements['succeeds'] in save_data.completed_levels
        ])

    @classmethod
    def from_yaml(cls, data):
        return cls(**data)


