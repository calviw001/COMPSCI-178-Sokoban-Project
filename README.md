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
