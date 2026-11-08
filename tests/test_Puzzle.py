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


def readBoard(fileName):
    with open(os.path.join(CURRDIR, "test_puzzles", fileName), "r") as f:
        lines = [line.rstrip("\n") for line in f]
    player = None
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char in "@+":
                player = (row + 1, col + 1)
    return lines, player


def loadEmptyPuzzle(goals=(), deadlocks=()):
    p = load("emptyPuzzle.txt")
    p.goals = set(goals)
    p.deadlocks = set(deadlocks) 
    return p


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
        self.assertEqual(p1.deadlocks, {(2, 2)})

        p2 = load("medium.txt")
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
        self.assertEqual(p3.deadlocks, {(3, 2), (3, 6)})


    def test_reachable_squares(self):
        p1 = load("small.txt")
        reachables = p1.allReachableSquares(p1.startState)
        self.assertEqual(reachables, {(2, 2)})
        print()

        p2 = load("medium.txt")
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
        self.assertFalse(p1.hasReachedGoal(p1.startState))
        # Small puzzle now solved
        p1 = load("smallSolved.txt")
        self.assertTrue(p1.hasReachedGoal(p1.startState))

        p2 = load("medium.txt")
        self.assertFalse(p2.hasReachedGoal(p2.startState))
        # Medium puzzle now solved
        p2 = load("mediumSolved.txt")
        self.assertTrue(p2.hasReachedGoal(p2.startState))


    def test_all_pushes(self):
        p1 = load("small.txt")
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
        pushables = p2.allPushes(p2.startState)
        self.assertEqual(pushables, {(5, 6): {(-1, 0)}, (6, 5): {(0, -1)}})
  
        p3 = load("smallMixedSymbols.txt")
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
        pushables = p4.allPushes(p4.startState)
        self.assertEqual(pushables, {(2, 4): {(0, 1)}})


    def test_single_push(self):
        p1 = load("small.txt")
        newState = p1.applySinglePush(p1.startState, (3, 2), (1, 0))
        self.assertEqual(newState.boxes, {(4, 2)})
        self.assertTrue(p1.hasReachedGoal(newState))

        p2 = load("medium.txt")
        # Try out each possible box push and box push directions from the start state
        for box, directions in p2.allPushes(p2.startState).items():
            for eachDir in directions:
                newState = p2.applySinglePush(p2.startState, box, eachDir)
                expectedNewBox = (box[0] + eachDir[0], box[1] + eachDir[1])
                self.assertEqual(newState.boxes, (p2.startState.boxes - {box}) | {expectedNewBox})

        p3 = load("smallMixedSymbols.txt")
        # Apply a push to both boxes
        newState = p3.applySinglePush(p3.startState, (2, 3), (0, 1))
        self.assertEqual(newState.boxes, frozenset({(2, 4), (2, 6), (3, 3)}))
        newState = p3.applySinglePush(p3.startState, (3, 3), (0, 1))
        self.assertEqual(newState.boxes, frozenset({(2, 3), (2, 6), (3, 4)}))

        # Boxes can be pushed off goals too
        p4 = load("smallBoxOnGoal.txt")
        newState = p4.applySinglePush(p4.startState, (2, 4), (0, 1))
        self.assertEqual(newState.boxes, frozenset({(2, 5)}))


    def test_normalize_state(self):
        p1 = load("small.txt")
        reachables = p1.allReachableSquares(p1.startState)
        normalized = p1.normalizeState(p1.startState)
        self.assertEqual(normalized.boxes, p1.startState.boxes)
        self.assertEqual(normalized.player, (2, 2))
        # The player now pushes the box forward into the goal. The normalized state should then put the player back 
        # to square (2, 2)
        newState = p1.applySinglePush(p1.startState, (3, 2), (1, 0))
        self.assertEqual(newState.player, (2, 2))

        p2 = load("medium.txt")
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
        reachables = p4.allReachableSquares(p4.startState)
        normalized = p4.normalizeState(p4.startState)
        self.assertEqual(normalized.boxes, p4.startState.boxes)
        self.assertEqual(normalized.player, (2, 2))
        newState = p4.applySinglePush(p4.startState, (2, 4), (0, 1))
        self.assertEqual(newState.player, (2, 2))


    def test_heuristic_on_solved_states(self):
        p1 = load("smallSolved.txt")
        self.assertEqual(p1.heuristic(p1.startState), 0)

        p2 = load("mediumSolved.txt")
        self.assertEqual(p2.heuristic(p2.startState), 0)

        p3 = load("smallMixedSymbolsSolved.txt")
        self.assertEqual(p3.heuristic(p3.startState), 0)


    def test_heuristic_on_unsolved_states(self):
        p1 = load("small.txt")
        self.assertEqual(p1.heuristic(p1.startState), 1)

        p2 = load("medium.txt")
        self.assertEqual(p2.heuristic(p2.startState), 6)
        # From the start state, push box at (6, 5) to the left
        pushedLeft = p2.applySinglePush(p2.startState, (6, 5), (0, -1))
        self.assertEqual(p2.heuristic(pushedLeft), 5)
        # From the start state, push box at (5, 6) to up
        pushedUp = p2.applySinglePush(p2.startState, (5, 6), (-1, 0))
        self.assertEqual(p2.heuristic(pushedUp), 7)

        p3 = load("smallMixedSymbols.txt")
        self.assertEqual(p3.heuristic(p3.startState), 3)
        # Two out of the three boxes have been solved now
        newState = State(frozenset({(2, 2), (2, 6), (3, 3)}), (2, 4))
        self.assertEqual(p3.heuristic(newState), 2)


    def test_print_current_puzzle(self):
        for fileName in ["small.txt", "medium.txt", "smallMixedSymbols.txt", "smallBoxOnGoal.txt", "smallSolved.txt", "mediumSolved.txt", "smallMixedSymbolsSolved.txt", "smallDetour.txt"]:
            p1 = load(fileName)
            lines, player = readBoard(fileName)
            state = State(p1.startState.boxes, player)
            result = p1.printCurrentPuzzle(state)
            self.assertEqual(len(result), len(lines))
            for i in range(len(lines)):
                self.assertEqual("".join(result[i]), lines[i])


    def test_can_go_straight_into_goal(self):
        p1 = load("small.txt")
        self.assertTrue(p1.canGoStraightIntoGoal(p1.startState, (3, 2), (1, 0)))     

        p2 = load("smallDetour.txt")             
        # Box will run into a wall if pushed right                             
        self.assertFalse(p2.canGoStraightIntoGoal(p2.startState, (3, 4), (0, 1)))  
        # Box can now be pushed stright up into a goal
        goalBoundState = State(frozenset({(3, 6)}), (2, 2))   
        self.assertTrue(p2.canGoStraightIntoGoal(goalBoundState, (3, 6), (-1, 0))) 

        p3 = load("medium.txt")
        # Both legal start pushes run into a wall before any goal
        self.assertFalse(p3.canGoStraightIntoGoal(p3.startState, (5, 6), (-1, 0)))
        self.assertFalse(p3.canGoStraightIntoGoal(p3.startState, (6, 5), (0, -1)))

        p4 = load("smallMixedSymbols.txt")
        # First box has a box in the way, while the second box is all good
        self.assertFalse(p4.canGoStraightIntoGoal(p4.startState, (2, 3), (0, 1)))
        self.assertTrue(p4.canGoStraightIntoGoal(p4.startState, (3, 3), (0, 1)))


    def test_is_frozen_deadlock_with_two_boxes_against_wall_and_with_2x2_block(self):
        # Two boxes side by side against a wall tests:

        p1 = loadEmptyPuzzle()
        state = State(frozenset(((2, 4), (2, 5))), (5, 8)) 
        self.assertTrue(p1.isFrozenDeadlock(state, (2, 5)))
        self.assertTrue(p1.isFrozenDeadlock(state, (2, 4)))

        # Frozen but both on goals: exactly where they should be, so no deadlock
        p2 = loadEmptyPuzzle(goals={(2, 4), (2, 5)})
        self.assertFalse(p2.isFrozenDeadlock(state, (2, 5)))

        # Frozen with only one on a goal: the other is stuck off its goal, so deadlock
        p3 = loadEmptyPuzzle(goals={(2, 4)})
        self.assertTrue(p3.isFrozenDeadlock(state, (2, 5)))

        # 2x2 block tests:

        p4 = loadEmptyPuzzle()
        state = State(frozenset(((3, 4), (3, 5), (4, 4), (4, 5))), (5, 8))
        self.assertTrue(p4.isFrozenDeadlock(state, (4, 5)))

        # All four are on boxes this time, so no deadlock
        p5 = loadEmptyPuzzle(goals={(3, 4), (3, 5), (4, 4), (4, 5)})
        self.assertFalse(p5.isFrozenDeadlock(state, (4, 5)))\
        
        # Three of four boxes are on goals, which still leaves one frozen box
        p6 = loadEmptyPuzzle(goals={(3, 4), (3, 5), (4, 4)})
        self.assertTrue(p6.isFrozenDeadlock(state, (4, 5)))


    def test_is_frozen_deadlock_with_single_box_and_adjacent_boxes_and_unfrozen_neighbor(self):
        # Single box against a wall can still slide
        p1 = loadEmptyPuzzle()
        state = State(frozenset(((2, 5))), (5, 8))
        self.assertFalse(p1.isFrozenDeadlock(state, (2, 5)))

        # Single box is simply placed around the center of the puzzle with nothing blocking it
        state = State(frozenset(((4, 5))), (5, 8))
        self.assertFalse(p1.isFrozenDeadlock(state, (4, 5)))      # open floor

        # Adjacent boxes side by side can still be pushed vertically if not against a wall
        p2 = loadEmptyPuzzle()
        state = State(frozenset(((3, 4), (3, 5))), (5, 8))
        self.assertFalse(p2.isFrozenDeadlock(state, (3, 5)))

        # (3,5) and (4,5) are frozen by the dead squares beside them and both sit on goals.
        # (2,5) is above them but is free to slide sideways, so it is NOT frozen.
        p3 = loadEmptyPuzzle(goals={(3, 5), (4, 5)}, deadlocks={(3, 4), (3, 6), (4, 4), (4, 6)})
        state = State(frozenset(((2, 5), (3, 5), (4, 5))), (5, 8))
        self.assertFalse(p3.isFrozenDeadlock(state, (3, 5)))


    def test_is_frozen_deadlock_with_surrounding_deadlocks(self):
        # Box should be frozen when there are deadlocks along both horizontal sides and both vertical sides
        p1 = loadEmptyPuzzle(deadlocks={(3, 4), (3, 6), (2, 5), (4, 5)})
        state = State(frozenset(((3, 5))), (5, 8))
        self.assertTrue(p1.isFrozenDeadlock(state, (3, 5)))

        # If only one side on an axis has deadlocks, then that still leaves the box free to move the other way
        p2 = loadEmptyPuzzle(deadlocks={(3, 4)})
        self.assertFalse(p2.isFrozenDeadlock(state, (3, 5)))


if __name__ == "__main__":
    unittest.main()