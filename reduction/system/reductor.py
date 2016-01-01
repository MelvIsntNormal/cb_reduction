# This is where reduction is implemented. This file handles checking and reducing atoms
from reduction.component.atom import Atom


def equality_reduction(a1, a2):
    if a1.essence == a2.essence:
        return a1.essence
    else:
        return None

methods = {
    'equality': equality_reduction
}


def can_reduce(a1, a2, method=equality_reduction):
    if not(isinstance(a1, Atom) and isinstance(a2, Atom)):
        raise ValueError("Only Atoms can be reduced")
    return method(a1, a2) is not None


def reduce_atoms(a1, a2, method=equality_reduction):
    if not(isinstance(a1, Atom) and isinstance(a2, Atom)):
        raise ValueError("Only Atoms can be reduced")

    essence = method(a1, a2)
    ions = a1.ions + a2.ions
    board_pos = a1.board_pos

    return Atom(essence, ions, board_pos)
