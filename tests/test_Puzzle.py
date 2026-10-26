import os
import sys
CURRDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRDIR))

import unittest
from Puzzle import Puzzle
from State import State


def load(fileName):
    puzzle = Puzzle()
    puzzle.parsePuzzleFile(os.path.join(CURRDIR, "test_puzzles", fileName))
    return puzzle


class TestPuzzleClass(unittest.TestCase):

    def test_parse_small_puzzle(self):
        p1 = load("small.txt")
        self.assertEqual((p1.height, p1.width), (5, 3))
        self.assertEqual(p1.goals, {(4, 2)})
        self.assertEqual(p1.startState.boxes, frozenset({(3, 2)}))
        self.assertEqual(p1.startState.player, (2, 2))
        self.assertEqual(len(p1.walls), 12)
        self.assertEqual(p1.floorSpaces, {(2, 2), (3, 2), (4, 2)})


    def test_parse_medium_puzzle(self):
        p2 = load("medium.txt")
        self.assertEqual((p2.height, p2.width), (8, 8))
        self.assertEqual(p2.goals, {(2, 2), (5, 7), (7, 4)})
        self.assertEqual(p2.startState.boxes, frozenset({(3, 4), (5, 6), (6, 5)}))
        self.assertEqual(p2.startState.player, (7, 7))
        expectedFloors = {
            (2, 2), (2, 3), (2, 5), (2, 6), (2, 7),
            (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
            (4, 2), (4, 3), (4, 4), (4, 6),
            (5, 3), (5, 5), (5, 6), (5, 7),
            (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7),
            (7, 2), (7, 3), (7, 4), (7, 6), (7, 7),
        }
        self.assertEqual(p2.floorSpaces, expectedFloors)


    def test_box_and_player_on_goal(self):
        # '*' counts as a box and a goal
        # '+' counts as the player and a goal
        p3 = load("smallMixedSymbols.txt")
        self.assertEqual((p3.height, p3.width), (4, 7))
        self.assertEqual(p3.startState.player, (2, 2))
        self.assertEqual(p3.startState.boxes, frozenset({(2, 3), (2, 6), (3, 3)}))
        self.assertEqual(p3.goals, {(2, 2), (2, 6), (3, 5)})
        expectedFloors = {
            (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
            (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
        }
        self.assertEqual(p3.floorSpaces, expectedFloors)


if __name__ == "__main__":
    unittest.main()