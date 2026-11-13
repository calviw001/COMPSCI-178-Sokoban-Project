import os
import sys
import tempfile
import unittest
from pathlib import Path

CURRDIR = os.path.dirname(os.path.abspath(__file__))
PROJECTDIR = os.path.dirname(CURRDIR)
sys.path.insert(0, os.path.join(PROJECTDIR, "python"))
sys.path.insert(0, PROJECTDIR)

from Puzzle import Puzzle
from sokoban_generator import generate


class TestSokobanGenerator(unittest.TestCase):
    def test_generated_board_round_trips_through_project_parser(self):
        level = generate(difficulty=1, seed=42, max_attempts=100, time_budget=5)
        board = level.ascii()

        self.assertTrue(level.verify())
        rows = board.splitlines()
        self.assertTrue(rows)
        self.assertEqual(len({len(row) for row in rows}), 1)

        with tempfile.NamedTemporaryFile(mode="w", suffix=".txt") as board_file:
            board_file.write(board + "\n")
            board_file.flush()

            puzzle = Puzzle()
            puzzle.parsePuzzleFile(board_file.name)

        self.assertEqual(len(puzzle.floorSpaces), len(level.floors))
        row_shift = 2 - min(row for row, _ in level.floors)
        col_shift = 2 - min(col for _, col in level.floors)
        translated = lambda cells: {
            (row + row_shift, col + col_shift) for row, col in cells
        }
        self.assertEqual(puzzle.startState.boxes, frozenset(translated(level.boxes)))
        self.assertEqual(puzzle.goals, translated(level.goals))


if __name__ == "__main__":
    unittest.main()
