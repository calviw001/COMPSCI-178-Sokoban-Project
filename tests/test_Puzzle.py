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
        self.assertEqual(p2.startState.player, (5, 7))
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


    def test_find_deadlocks(self):
        p1 = load("small.txt")
        p1.findDeadlocks()
        self.assertEqual(p1.deadlocks, {(2, 2)})

        p2 = load("medium.txt")
        p2.findDeadlocks()
        expectedDeadlocks = {
            (2, 3), (2, 5), (2, 6), (2, 7),
            (3, 7),
            (4, 2), (4, 4),
            (5, 5),
            (6, 2),
            (7, 2), (7, 6), (7, 7),
        }
        self.assertEqual(p2.deadlocks, expectedDeadlocks)

        p3 = load("smallMixedSymbols.txt")
        p3.findDeadlocks()
        self.assertEqual(p3.deadlocks, {(3, 2), (3, 6)})


    def test_reachable_squares(self):
        p1 = load("small.txt")
        reachables = p1.allReachableSquares(p1.startState)
        self.assertEqual(reachables, {(2, 2)})
        print()

        p2 = load("medium.txt")
        p2.findDeadlocks()
        reachables = p2.allReachableSquares(p2.startState)
        self.assertEqual(reachables, {(7, 7), (7, 6), (6, 7), (6, 6), (5, 7)})
        # State after Player pushes box at (6,4) to the left, so the box is now at (6,5)
        leftBoxPushState = State(frozenset({(3, 4), (5, 6), (6, 4)}), (7, 7))    
        reachables = p2.allReachableSquares(leftBoxPushState)
        self.assertEqual(reachables, {(7, 7), (7, 6), (6, 7), (6, 6), (5, 7), (6, 5), (5, 5)})

        p3 = load("smallMixedSymbols.txt")
        reachables = p3.allReachableSquares(p3.startState)
        self.assertEqual(reachables, {(2, 2), (3, 2)})

        p4 = load("smallBoxOnGoal.txt")
        reachables = p4.allReachableSquares(p4.startState)
        self.assertEqual(reachables, {(2, 2), (2, 3)})
        # Make sure that the function did not include the goal square because a box is on top of it
        self.assertNotIn((2, 4), reachables) 


    def test_has_reached_goal(self):
        p1 = load("small.txt")
        p1.findDeadlocks()
        self.assertFalse(p1.hasReachedGoal(p1.startState))
        # Small puzzle now solved
        p1 = load("smallSolved.txt")
        p1.findDeadlocks()
        self.assertTrue(p1.hasReachedGoal(p1.startState))

        p2 = load("medium.txt")
        p2.findDeadlocks()
        self.assertFalse(p2.hasReachedGoal(p2.startState))
        # Medium puzzle now solved
        p2 = load("mediumSolved.txt")
        p2.findDeadlocks()
        self.assertTrue(p2.hasReachedGoal(p2.startState))


    def test_all_pushes(self):
        p1 = load("small.txt")
        p1.findDeadlocks()
        pushables = p1.allPushes(p1.startState)
        self.assertEqual(pushables, {(3, 2): {(1, 0)}})
        # Player can now only push box into a deadlock
        deadlockPushState = State(frozenset({(3, 2)}), (4, 2))
        pushables = p1.allPushes(deadlockPushState)
        # Make sure that the function does not included pushes in deadlocks
        self.assertEqual(pushables, {})
        # Player can now only push box into a wall
        wallPushState = State(frozenset({(4, 2)}), (2, 2))
        pushables = p1.allPushes(wallPushState)
        # Make sure that the function does not included pushes into walls
        self.assertEqual(pushables, {})

        p2 = load("medium.txt")
        p2.findDeadlocks()
        pushables = p2.allPushes(p2.startState)
        self.assertEqual(pushables, {(5, 6): {(-1, 0)}, (6, 5): {(0, -1)}})
  
        p3 = load("smallMixedSymbols.txt")
        p3.findDeadlocks()
        pushables = p3.allPushes(p3.startState)
        self.assertEqual(pushables, {(2, 3): {(0, 1)}, (3, 3): {(0, 1)}})
        # Only the box at (3,5) can be pushed to the left
        onlyOneLeftPushableBoxState = State(frozenset({(3, 5)}), (3, 4))
        pushables = p3.allPushes(onlyOneLeftPushableBoxState)
        # Make sure the function returns only this one left push
        self.assertEqual(pushables, {(3, 5): {(0, -1)}})
        # Now both boxes can no longer be pushed
        noMorePushesState = State(frozenset({(2, 3), (2, 4)}), (2, 2))
        pushables = p3.allPushes(noMorePushesState)
        # Make sure that the function does not any pushes
        self.assertEqual(pushables, {})

        # Boxes can be pushed off goals too
        p4 = load("smallBoxOnGoal.txt")
        p4.findDeadlocks()
        pushables = p4.allPushes(p4.startState)
        self.assertEqual(pushables, {(2, 4): {(0, 1)}})


    def test_single_push(self):
        p1 = load("small.txt")
        p1.findDeadlocks()
        newState = p1.applySinglePush(p1.startState, (3, 2), (1, 0))
        self.assertEqual(newState.boxes, {(4, 2)})
        self.assertTrue(p1.hasReachedGoal(newState))

        p2 = load("medium.txt")
        p2.findDeadlocks()
        # Try out each possible box push and box push directions from the start state
        for box, directions in p2.allPushes(p2.startState).items():
            for eachDir in directions:
                newState = p2.applySinglePush(p2.startState, box, eachDir)
                expectedNewBox = (box[0] + eachDir[0], box[1] + eachDir[1])
                self.assertEqual(newState.boxes, (p2.startState.boxes - {box}) | {expectedNewBox})

        p3 = load("smallMixedSymbols.txt")
        p3.findDeadlocks()
        # Apply a push to both boxes
        newState = p3.applySinglePush(p3.startState, (2, 3), (0, 1))
        self.assertEqual(newState.boxes, frozenset({(2, 4), (2, 6), (3, 3)}))
        newState = p3.applySinglePush(p3.startState, (3, 3), (0, 1))
        self.assertEqual(newState.boxes, frozenset({(2, 3), (2, 6), (3, 4)}))

        # Boxes can be pushed off goals too
        p4 = load("smallBoxOnGoal.txt")
        p4.findDeadlocks()
        newState = p4.applySinglePush(p4.startState, (2, 4), (0, 1))
        self.assertEqual(newState.boxes, frozenset({(2, 5)}))


    def test_single_push(self):
        p1 = load("small.txt")
        p1.findDeadlocks()
        reachables = p1.allReachableSquares(p1.startState)
        normalized = p1.normalizeState(p1.startState)
        self.assertEqual(normalized.boxes, p1.startState.boxes)
        self.assertEqual(normalized.player, (2, 2))
        # The player now pushes the box forward into the goal. The normalized state should then put the player back 
        # to square (2, 2)
        newState = p1.applySinglePush(p1.startState, (3, 2), (1, 0))
        self.assertEqual(newState.player, (2, 2))

        p2 = load("medium.txt")
        p2.findDeadlocks()
        reachables = p2.allReachableSquares(p2.startState)
        normalized = p2.normalizeState(p2.startState)
        self.assertEqual(normalized.boxes, p2.startState.boxes)
        self.assertIn(normalized.player, reachables)
        # Have each state place the player into a different reachable square
        # After normalizing each state, they should all be eqivalent
        normalizedStates = {p2.normalizeState(State(p2.startState.boxes, square)) for square in reachables}
        self.assertEqual(len(normalizedStates), 1)
        self.assertEqual(normalizedStates, {State(p2.startState.boxes, (5, 7))})

        p3 = load("smallMixedSymbols.txt")
        p3.findDeadlocks()
        reachables = p3.allReachableSquares(p3.startState)
        normalized = p3.normalizeState(p3.startState)
        self.assertEqual(normalized.boxes, p3.startState.boxes)
        self.assertIn(normalized.player, reachables)
        # Normalize two states where one state has the player start at (2, 2) while the other state has the player start at (2, 3) 
        # The two normalized should equal because the players will have the same reachables region in both states
        normalized1 = p3.normalizeState(State(p3.startState.boxes, (2, 2)))
        normalized2 = p3.normalizeState(State(p3.startState.boxes, (3, 2)))
        self.assertEqual(normalized1, normalized2)
        self.assertEqual(hash(normalized1), hash(normalized2))

        # # Boxes can be pushed off goals too
        p4 = load("smallBoxOnGoal.txt")
        p4.findDeadlocks()
        reachables = p4.allReachableSquares(p4.startState)
        normalized = p4.normalizeState(p4.startState)
        self.assertEqual(normalized.boxes, p4.startState.boxes)
        self.assertEqual(normalized.player, (2, 2))
        newState = p4.applySinglePush(p4.startState, (2, 4), (0, 1))
        self.assertEqual(newState.player, (2, 2))
            

if __name__ == "__main__":
    unittest.main()