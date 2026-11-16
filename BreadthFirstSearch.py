"""Push-based breadth-first search for Sokoban puzzles."""

from collections import deque
from math import inf
from time import perf_counter


class BreadthFirstSearch:
    """Find a minimum-push solution using an unweighted FIFO search."""

    def __init__(self, puzzle, time_limit=None):
        self.puzzle = puzzle
        self.time_limit = time_limit
        self.nodes_expanded = 0
        self.elapsed_seconds = 0.0
        self._deadline = inf

    def solve(self):
        """Return push actions, ``[]`` if solved, or ``None`` if unsolvable."""
        if self.time_limit is not None and self.time_limit <= 0:
            raise ValueError("time_limit must be positive")

        started = perf_counter()
        self.nodes_expanded = 0
        self._deadline = (
            started + self.time_limit if self.time_limit is not None else inf
        )

        try:
            self.puzzle.findDeadlocks()
            start_state = self.puzzle.normalizeState(self.puzzle.startState)
            if self.puzzle.isDeadlocked(start_state):
                return None

            frontier = deque([start_state])
            parents = {start_state: None}

            while frontier:
                self._check_time()
                state = frontier.popleft()
                if self.puzzle.hasReachedGoal(state):
                    return self._reconstruct_path(state, parents)

                self.nodes_expanded += 1
                pushable = self.puzzle.allPushes(state)
                for box in sorted(pushable):
                    for direction in sorted(pushable[box]):
                        next_state = self.puzzle.applySinglePush(state, box, direction)
                        if next_state in parents:
                            continue
                        if self.puzzle.isDeadlocked(next_state):
                            continue

                        parents[next_state] = (state, (box, direction))
                        frontier.append(next_state)

            return None
        finally:
            self.elapsed_seconds = perf_counter() - started

    def _check_time(self):
        if perf_counter() >= self._deadline:
            raise TimeoutError("BFS time limit exceeded")

    @staticmethod
    def _reconstruct_path(state, parents):
        path = []
        while parents[state] is not None:
            parent, action = parents[state]
            path.append(action)
            state = parent
        path.reverse()
        return path
