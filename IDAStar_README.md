# IDA* solver

Based on Section 4.1 of *Willy: A Sokoban Solving Agent*.
Finds a solution with the fewest box pushes using `g + h` thresholds.

```python
from IDAStar import IDAStar

solution = IDAStar(puzzle).solve()
```

- Returns `(box_position, direction)` pairs, using `(row, column)` coordinates.
- `[]`: already solved. `None`: no solution.
- Optional: `IDAStar(puzzle, time_limit=30)`; timeout raises `TimeoutError`.
- Uses `Puzzle` for legal pushes, static dead squares, and the matching heuristic.

Run through `Main.py`; see `README.md` for commands.
