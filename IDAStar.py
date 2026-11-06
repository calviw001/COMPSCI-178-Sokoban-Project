"""
Push-optimal IDA* for Puzzle.py (Willy).

Run it at Main.py.
"""

from math import inf
from time import perf_counter


class IDAStar:
    """
    Return [(box_position_before_push, direction), ...], or None if unsolvable.

    Each push costs one; walking has no cost.
    """

    def __init__(self, puzzle, time_limit=None):
        self.puzzle = puzzle
        self.time_limit = time_limit
        self.nodes_expanded = 0
        self.thresholds = []  # for testing
        self.elapsed_seconds = 0.0


    def solve(self):
        """Search without changing the starting state; [] means already solved."""
        # reset solver
        self.nodes_expanded = 0
        self.thresholds = []
        self.push_sequence = []
        start_time = perf_counter()

        # set time limit
        if self.time_limit is not None:
            self.deadline = start_time + self.time_limit

        else:
            self.deadline = inf

        try:
            # the parsePuzzleFile() function already normalizes the start state
            start_state = self.puzzle.startState        
            self.puzzle.findDeadlocks()

            # check deadlock before start
            if start_state.boxes & self.puzzle.deadlocks:
                return None
            
            # first threshold = h
            threshold = self.puzzle.heuristic(start_state)
            while threshold < inf:
                self.check_time()
                self.thresholds.append(threshold)

                # reset min pushes each round
                self.min_pushes = {}

                # run the search
                # if true, a solution was found and we don't need to go another round
                search_result = self.search(start_state, 0, threshold)
                if search_result is True:
                    return self.push_sequence.copy()
                
                # next round uses the smallest exceeded f
                threshold = search_result
            return None
        finally:
            self.elapsed_seconds = perf_counter() - start_time


    # It raises TimeoutError if the deadline has passed. Main.py catches that error.
    def check_time(self):
        if perf_counter() >= self.deadline:
            raise TimeoutError("IDA* time limit exceeded")


    # Returns True = solved, a number = the smallest f that exceeded the threshold, or inf = nothing useful here
    def search(self, state, g, threshold): 
        self.check_time()

        # g = pushes so far, h = estimated pushes left
        f = g + self.puzzle.heuristic(state)

        # over threshold, stop this branch
        if f > threshold:
            return f

        # return True if reached goal state
        if self.puzzle.hasReachedGoal(state):
            return True

        # skip if already reached with fewer or equal pushes
        if self.min_pushes.get(state, inf) <= g:
            return inf
        
        self.min_pushes[state] = g
        self.nodes_expanded += 1
        next_threshold = inf
        pushes = self.puzzle.allPushes(state)

        for box in sorted(pushes):
            for direction in sorted(pushes[box]):
                next_state = self.puzzle.applySinglePush(state, box, direction)
                self.push_sequence.append((box, direction))
                search_result = self.search(next_state, g + 1, threshold)
                if search_result is True:
                    return True
                
                # backtrack
                self.push_sequence.pop()
                next_threshold = min(next_threshold, search_result)

        return next_threshold
