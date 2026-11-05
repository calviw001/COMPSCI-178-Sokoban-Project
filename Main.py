import argparse
from pathlib import Path

from IDAStar import IDAStar
from Puzzle import Puzzle


def solve_file(puzzle_path, time_limit=None):
    puzzle = Puzzle()
    puzzle.parsePuzzleFile(puzzle_path)
    solver = IDAStar(puzzle, time_limit=time_limit)

    print(f"Puzzle: {puzzle_path}")
    print("Initial board:")
    puzzle.printCurrentPuzzle(puzzle.startState)

    try:
        solution = solver.solve()
    except TimeoutError:
        print("Result: timed out")
    else:
        if solution is None:
            print("Result: no solution")
        else:
            state = puzzle.startState
            for step, (box, direction) in enumerate(solution, start=1):
                state = puzzle.applySinglePush(state, box, direction)
                print(f"Push {step}: box={box}, direction={direction}")
                puzzle.printCurrentPuzzle(state)
            print(f"Result: solved in {len(solution)} pushes")

    print(f"Expanded states: {solver.nodes_expanded}")
    print(f"Elapsed seconds: {solver.elapsed_seconds:.6f}")
    return solution


def main():
    parser = argparse.ArgumentParser(description="Solve a Sokoban puzzle with IDA*")
    parser.add_argument("path", type=Path, help="path to a Sokoban board text file")
    parser.add_argument(
        "--time-limit",
        type=float,
        default=None,
        metavar="SECONDS",
        help="stop searching after the specified number of seconds",
    )
    args = parser.parse_args()
    if args.time_limit is not None and args.time_limit <= 0:
        parser.error("--time-limit must be positive")
    if not args.path.is_file():
        parser.error(f"board file does not exist: {args.path}")

    try:
        solve_file(args.path, args.time_limit)
    except (OSError, UnicodeError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
