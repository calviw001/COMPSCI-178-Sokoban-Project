# COMPSCI-178-Sokoban-Project

Run commands from the project root.

## Command

```bash

usage: Main.py [-h] [--time-limit SECONDS] [path]

# File (replace xxx.txt with your map filename)
python Main.py tests/test_puzzles/xxx.txt

# Folder
python Main.py tests/test_puzzles

# File with a 30-second time limit
python Main.py tests/test_puzzles/xxx.txt --time-limit 30

# Folder with a 30-second time limit per map
python Main.py tests/test_puzzles --time-limit 30

# Default map (medium.txt)
python Main.py

# Help
python Main.py --help

```

## Performance

Measured with the existing IDA* solver, without a time limit. Times are measured inside `solve()` and exclude imports, map parsing, and independent solution validation. Boards were tested sequentially within each set; these are individual run times, not averages.

All 16 generated boards were solved and independently replayed to verify legal pushes and that all boxes finished on goals.

| Test folder | Input | Boxes | Pushes | Expanded states | Solve time (s) |
|---|---|---:|---:|---:|---:|
| [tests/7x7](tests/7x7) | [irregular_01.txt](tests/7x7/irregular_01.txt) | 2 | 10 | 39 | 0.003993 |
| [tests/7x7](tests/7x7) | [irregular_02.txt](tests/7x7/irregular_02.txt) | 3 | 7 | 8 | 0.001172 |
| [tests/7x7](tests/7x7) | [irregular_03.txt](tests/7x7/irregular_03.txt) | 2 | 7 | 7 | 0.000848 |
| [tests/7x7](tests/7x7) | [irregular_04.txt](tests/7x7/irregular_04.txt) | 3 | 7 | 8 | 0.001207 |
| [tests/7x7](tests/7x7) | [irregular_05.txt](tests/7x7/irregular_05.txt) | 3 | 6 | 6 | 0.000818 |
| [tests/8x8](tests/8x8) | [custom_8x8_01.txt](tests/8x8/custom_8x8_01.txt) | 3 | 13 | 275 | 0.284968 |
| [tests/8x8](tests/8x8) | [custom_8x8_02.txt](tests/8x8/custom_8x8_02.txt) | 3 | 11 | 11 | 0.007111 |
| [tests/8x8](tests/8x8) | [custom_8x8_03.txt](tests/8x8/custom_8x8_03.txt) | 3 | 11 | 11 | 0.004697 |
| [tests/8x8](tests/8x8) | [custom_8x8_04.txt](tests/8x8/custom_8x8_04.txt) | 3 | 9 | 9 | 0.005982 |
| [tests/8x8](tests/8x8) | [custom_8x8_05.txt](tests/8x8/custom_8x8_05.txt) | 3 | 9 | 30 | 0.022127 |
| [tests/9x9](tests/9x9) | [board_9x9_01.txt](tests/9x9/board_9x9_01.txt) | 4 | 18 | 2825 | 3.087334 |
| [tests/9x9](tests/9x9) | [board_9x9_02.txt](tests/9x9/board_9x9_02.txt) | 4 | 16 | 128 | 0.136355 |
| [tests/9x9](tests/9x9) | [board_9x9_03.txt](tests/9x9/board_9x9_03.txt) | 4 | 19 | 4588 | 5.248016 |
| [tests/10x10](tests/10x10) | [board_10x10_01.txt](tests/10x10/board_10x10_01.txt) | 4 | 17 | 2023 | 3.384264 |
| [tests/10x10](tests/10x10) | [board_10x10_02.txt](tests/10x10/board_10x10_02.txt) | 4 | 17 | 754 | 1.079881 |
| [tests/10x10](tests/10x10) | [board_10x10_03.txt](tests/10x10/board_10x10_03.txt) | 4 | 26 | 10610 | 14.564055 |

The `7x7` set has irregular, fully enclosed outlines and variable line lengths. Each board has a maximum height and width of 7.

Run a test folder from the project root:

```bash
python Main.py tests/7x7
python Main.py tests/8x8
python Main.py tests/9x9
python Main.py tests/10x10
```
