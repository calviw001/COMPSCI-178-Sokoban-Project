"""Push-based IDA* search for Sokoban puzzles."""

from math import inf
from time import perf_counter


class IDAStar:
    """Find a solution measured in box pushes using iterative-deepening A*."""

    def __init__(self, puzzle, time_limit=None):
        self.puzzle = puzzle
        self.time_limit = time_limit
        self.nodes_expanded = 0
        self.thresholds = []
        self.elapsed_seconds = 0.0
        self._deadline = inf
        self._minimum_g = {}
        self._path = []

    def solve(self):
        """Return push actions, ``[]`` for an already-solved board, or ``None``."""
        if self.time_limit is not None and self.time_limit <= 0:
            raise ValueError("time_limit must be positive")

        started = perf_counter()
        self.nodes_expanded = 0
        self.thresholds = []
        self._path = []
        self._minimum_g = {}
        self._deadline = (
            started + self.time_limit if self.time_limit is not None else inf
        )

        try:
            self.puzzle.findDeadlocks()
            start_state = self.puzzle.normalizeState(self.puzzle.startState)
            if start_state.boxes & self.puzzle.deadlocks:
                return None

            threshold = self.puzzle.heuristic(start_state)
            while threshold != inf:
                self._check_time()
                self.thresholds.append(threshold)
                self._minimum_g.clear()
                result = self._search(start_state, 0, threshold)
                if result is True:
                    return list(self._path)
                if result == inf:
                    return None
                threshold = result
        finally:
            self.elapsed_seconds = perf_counter() - started

    def _check_time(self):
        if perf_counter() >= self._deadline:
            raise TimeoutError("IDA* time limit exceeded")

    def _search(self, state, pushes, threshold):
        self._check_time()
        estimated_total = pushes + self.puzzle.heuristic(state)
        if estimated_total > threshold:
            return estimated_total
        if self.puzzle.hasReachedGoal(state):
            return True

        previous_pushes = self._minimum_g.get(state)
        if previous_pushes is not None and previous_pushes <= pushes:
            return inf
        self._minimum_g[state] = pushes
        self.nodes_expanded += 1

        next_threshold = inf
        pushable = self.puzzle.allPushes(state)
        for box in sorted(pushable):
            for direction in sorted(pushable[box]):
                next_state = self.puzzle.applySinglePush(state, box, direction)
                self._path.append((box, direction))
                result = self._search(next_state, pushes + 1, threshold)
                if result is True:
                    return True
                self._path.pop()
                next_threshold = min(next_threshold, result)
        return next_threshold
