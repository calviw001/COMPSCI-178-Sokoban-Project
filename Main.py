"""Run a Sokoban solver and print its search statistics."""
import argparse
from pathlib import Path
import sys

from IDAStar import IDAStar
from Puzzle import Puzzle
from State import State


def main():
    # Keep the original path-only form as IDA* with all optimizations.
    argv = sys.argv[1:]
    explicit_ida = bool(argv and argv[0] == "ida")
    if explicit_ida:
        argv.pop(0)
    parser = argparse.ArgumentParser(
        description="Solve Sokoban with IDA*",
        usage="%(prog)s [ida] [path] [-d] [-s] [-f] [--time-limit SECONDS]",
    )
    parser.add_argument("path", nargs="?", type=Path, default=(
        Path(__file__).resolve().parent / "tests" / "test_puzzles" / "medium.txt"),
        help="map file or folder containing .txt maps")
    parser.add_argument("--time-limit", type=float, default=None, metavar="SECONDS",
                        help="time limit for each map")
    parser.add_argument("-d", action="store_true", help="enable static deadlock detection")
    parser.add_argument("-s", action="store_true", help="enable move sorting")
    parser.add_argument("-f", action="store_true", help="enable frozen-block detection")
    args = parser.parse_args(argv)
    flags = (args.d, args.s, args.f)
    if not explicit_ida and any(flags):
        parser.error("-d, -s and -f require the ida mode")
    if not explicit_ida:
        flags = (True, True, True)

    if args.time_limit is not None and args.time_limit <= 0:
        parser.error("--time-limit must be positive")

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

    # solve each file
    solved_files = []
    for puzzle_file in files:
        print(f"\n=== {puzzle_file} ===", flush=True)

        try:
            solve_file(puzzle_file, args.time_limit, flags=flags)
            solved_files.append(puzzle_file.name)
        except (OSError, UnicodeError, ValueError) as error:
            print(f"Could not solve {puzzle_file.name}: {error}")
            if len(files) == 1:
                raise SystemExit(1)
            
    for each in solved_files:
        print(each)


def solve_file(puzzle_file, time_limit=None, quiet=True, *,
               flags=(True, True, True)):
    """Print the board and search statistics for one map."""
    board_text = puzzle_file.read_text()
    deadlock, sorting, frozen = flags
    puzzle = Puzzle(useDeadlocks=deadlock, sortStates=sorting, checkFrozenBox=frozen)
    puzzle.parsePuzzleFile(puzzle_file)

    print("Initial board:")
    print(board_text.rstrip("\n"))
    print(flush=True)
    solver = IDAStar(puzzle, time_limit=time_limit)

    try:
        solution = solver.solve()

    except TimeoutError:
        print("Time limit reached; no solution found within the limit.")

    else:
        if solution is None:
            print("No solution exists.")
        else:
            print(f"Solved: {len(solution)} pushes")
        if solution is not None and not quiet:
            state = puzzle.startState
            for step, (box, direction) in enumerate(solution, 1):
                next_state = puzzle.applySinglePush(state, box, direction)
                # After a push, the player stands where the box was.
                state = State(next_state.boxes, box)
                print(f"Step {step}:")
                puzzle.printCurrentPuzzle(state)

    print(f"Expanded states: {solver.nodes_expanded}")
    print(f"Running time: {solver.elapsed_seconds:.6f} seconds")


if __name__ == "__main__":
    main()
