"""
command line input
 Main.py [-h] [--time-limit SECONDS] [--output FILE] [path]
output:
    print board states
"""
import argparse
from pathlib import Path
from IDAStar import IDAStar
from Puzzle import Puzzle
from State import State
from contextlib import redirect_stdout, nullcontext


def main():
    #parse the command line args
    # Main.py [-h] [--time-limit SECONDS] [--output FILE] [path]
    parser = argparse.ArgumentParser(description="Solve Sokoban with IDA*")
    parser.add_argument("path", nargs="?", type=Path, default=(
        Path(__file__).resolve().parent / "tests" / "test_puzzles" / "medium.txt"),
        help="map file or folder containing .txt maps")
    parser.add_argument("--time-limit", type=float, default=None, metavar="SECONDS",
                        help="time limit for each map")
    parser.add_argument("--output", type=Path, default=None, metavar="FILE",
                        help="also write everything printed to this file")
    args = parser.parse_args()

    if args.time_limit is not None and args.time_limit <= 0:
        parser.error("--time-limit must be positive")

    outputFile = None
    if args.output is not None:
        outputFile = open(args.output.expanduser(), "w", encoding="utf-8", buffering=1)

    #check path is file or folder
    target = args.path.expanduser()
    if target.is_file():
        files = [target]

    elif target.is_dir():
        files = []

        for file in target.iterdir():
            if file.is_file() and file.suffix.lower() == ".txt":
                files.append(file)

        files.sort()
        if not files:
            parser.error(f"No .txt map files found in: {target}")

    else:
        parser.error(f"File or folder does not exist: {target}")

    try:
        with redirect_stdout(outputFile) if outputFile else nullcontext():
            # solve each file
            solved_files = []
            for puzzle_file in files:
                print(f"\n=== {puzzle_file} ===", flush=True)

                try:
                    result = solve_file(puzzle_file, args.time_limit)
                    if result:
                        solved_files.append(puzzle_file.name)
                except (OSError, UnicodeError, ValueError) as error:
                    print(f"Could not solve {puzzle_file.name}: {error}")
                    if len(files) == 1:
                        raise SystemExit(1)

            print()
            print(f"Solved {len(solved_files)} out of {len(files)} puzzles:")
            for name in solved_files:
                print(f"  {name}")
    finally:
        if outputFile is not None:
            outputFile.close()


def solve_file(puzzle_file, time_limit=None, quiet=False):
    """Print the initial board and each solution push for one input file."""
    board_text = puzzle_file.read_text()
    puzzle = Puzzle()
    puzzle.parsePuzzleFile(puzzle_file)

    puzzle.useDeadlocks = True
    puzzle.sortStates = True
    puzzle.checkFrozenBox = True
    quiet = True

    # print original board
    print("Initial board:")
    print(board_text.rstrip("\n"))
    print(flush=True)
    solver = IDAStar(puzzle, time_limit=time_limit)
    solved = False

    try:
        solution = solver.solve()

    except TimeoutError:
        print("Time limit reached; no solution found within the limit.")

    else:
        if solution is None:
            print("No solution exists.")
        else:
            solved = True
            state = puzzle.startState
            for step, (box, direction) in enumerate(solution, 1):
                # TODO: add BFS to print walking steps

                next_state = puzzle.applySinglePush(state, box, direction)
                # player ends at the old box position
                state = State(next_state.boxes, box)
                if not quiet:
                    print(f"Step {step}:")
                    puzzle.printCurrentPuzzle(state)
            print(f"Solved: {len(solution)} pushes")

    print(f"Expanded states: {solver.nodes_expanded}")
    print(f"Running time: {solver.elapsed_seconds:.6f} seconds")
    return solved


if __name__ == "__main__":
    main()
