# Three-box solver comparison

All eight IDA* configurations solved all 10 puzzles in each folder. Each configuration ran once per puzzle, sequentially, with no time limit.
The IDA* variants share the same minimum-matching heuristic.
Times cover the solver call, including solution reconstruction. Parsing and replay validation are outside the timed region.
Every solution was replayed, and all configurations agreed on the push count for each puzzle.

### Number of box pushes

| Puzzle folder (height × width, boxes) | Control (BFS) | IDA\* | IDA\* + deadlock | IDA\* + sorting | IDA\* + frozen block | IDA\* + deadlock + sorting | IDA\* + deadlock + frozen block | IDA\* + sorting + frozen block | IDA\* + all three |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [7x7_3box](7x7_3box/) (7 × 7, 3) |  | 16.5 | 16.5 | 16.5 | 16.5 | 16.5 | 16.5 | 16.5 | 16.5 |
| [8x8_3box](8x8_3box/) (8 × 8, 3) |  | 19.1 | 19.1 | 19.1 | 19.1 | 19.1 | 19.1 | 19.1 | 19.1 |
| [9x9_3box](9x9_3box/) (9 × 9, 3) |  | 22.8 | 22.8 | 22.8 | 22.8 | 22.8 | 22.8 | 22.8 | 22.8 |
| [10x10_3box](10x10_3box/) (10 × 10, 3) |  | 26.0 | 26.0 | 26.0 | 26.0 | 26.0 | 26.0 | 26.0 | 26.0 |

### Expanded states

| Puzzle folder (height × width, boxes) | Control (BFS) | IDA\* | IDA\* + deadlock | IDA\* + sorting | IDA\* + frozen block | IDA\* + deadlock + sorting | IDA\* + deadlock + frozen block | IDA\* + sorting + frozen block | IDA\* + all three |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [7x7_3box](7x7_3box/) (7 × 7, 3) |  | 125.5 | 125.5 | 111.1 | 122.8 | 111.1 | 122.8 | 108.8 | 108.8 |
| [8x8_3box](8x8_3box/) (8 × 8, 3) |  | 191.1 | 191.1 | 180.0 | 183.6 | 180.0 | 183.6 | 173.3 | 173.3 |
| [9x9_3box](9x9_3box/) (9 × 9, 3) |  | 799.5 | 799.5 | 677.9 | 760.4 | 677.9 | 760.2 | 643.0 | 642.8 |
| [10x10_3box](10x10_3box/) (10 × 10, 3) |  | 135.7 | 135.7 | 153.2 | 125.0 | 153.2 | 123.2 | 143.7 | 141.9 |

### Running time in seconds

| Puzzle folder (height × width, boxes) | Control (BFS) | IDA\* | IDA\* + deadlock | IDA\* + sorting | IDA\* + frozen block | IDA\* + deadlock + sorting | IDA\* + deadlock + frozen block | IDA\* + sorting + frozen block | IDA\* + all three |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| [7x7_3box](7x7_3box/) (7 × 7, 3) |  | 0.017598 | 0.010937 | 0.013651 | 0.016191 | 0.008585 | 0.012871 | 0.017206 | 0.010871 |
| [8x8_3box](8x8_3box/) (8 × 8, 3) |  | 0.023162 | 0.018689 | 0.025258 | 0.033448 | 0.013697 | 0.018486 | 0.021619 | 0.018761 |
| [9x9_3box](9x9_3box/) (9 × 9, 3) |  | 0.082453 | 0.060752 | 0.065379 | 0.089658 | 0.065157 | 0.093333 | 0.089677 | 0.061794 |
| [10x10_3box](10x10_3box/) (10 × 10, 3) |  | 0.023403 | 0.024309 | 0.026903 | 0.025414 | 0.024416 | 0.022002 | 0.034091 | 0.027900 |
