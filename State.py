from dataclasses import dataclass

@dataclass(frozen=True)
class State:
    """
    This data class will hold all the current positions of the boxes and the player position of a Sokoban puzzle. 
    There will be multiple instances of this class in order to keep track of the different States that our solver will explore.
    """
    boxes: frozenset
    player: tuple
