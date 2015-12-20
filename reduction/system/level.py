class Chapter:
    def __init__(self, _id, _title, _levels):
        self.title = _title
        self.levels = _levels

    @classmethod
    def from_yaml(cls,  data):
        id = data['id']
        title = data['title']
        levels = [Level.from_yaml(level) for level in data['levels']]
        return cls(id, title, levels)


class Level:
    def __init__(self, id, title, energy, atoms, world):
        self.id = id
        self.title = title
        self.energy = energy
        self.atoms = atoms
        self.world = world

    @classmethod
    def from_yaml(cls, data):
        return cls(**data)


