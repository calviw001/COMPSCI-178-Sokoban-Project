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

    def test_parse_medium_puzzle(self):
        p2 = load("medium.txt")
        self.assertEqual((p2.height, p2.width), (8, 8))
        self.assertEqual(p2.goals, {(2, 2), (5, 7), (7, 4)})
        self.assertEqual(p2.startState.boxes, frozenset({(3, 4), (5, 6), (6, 5)}))
        self.assertEqual(p2.startState.player, (7, 7))

    def test_box_and_player_on_goal(self):
        # '*' counts as a box and a goal
        # '+' counts as the player and a goal
        p3 = load("smallMixedSymbols.txt")
        self.assertEqual((p3.height, p3.width), (4, 7))
        self.assertEqual(p3.startState.player, (2, 2))
        self.assertEqual(p3.startState.boxes, frozenset({(2, 3), (2, 6), (3, 3)}))
        self.assertEqual(p3.goals, {(2, 2), (2, 6), (3, 5)})


if __name__ == "__main__":
    unittest.main()