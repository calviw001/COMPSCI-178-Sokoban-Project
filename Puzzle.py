from pathlib import Path
from State import State

class Puzzle:
    """
    This class will hold all information about a Sokoban puzzle that stays the same. 
    This includes wall positions, goal positions, the height of the puzzle, the width of the puzzle, static deadlock positions,
    and the starting state of the puzzle. 
    """

    def __init__(self, height=0, width=0, walls=set(), goals=set(), start=None):
        self.height = height
        self.width = width
        self.walls = set()
        self.goals = set()
        self.deadlocks = set()        # dead squares, filled by findDeadlocks()
        self.startState = start

    # Read in a Sokoban puzzle in the form of a text file. Parse each line of the file in order to extract the 
    # x and y coordinates of the different Sokoban elements and add that information to the Puzzle class.
    def parsePuzzleFile(self, puzzleFile):
        numRows = 0
        numCols = 0
        boxes = set()
        player = None

        # Open the puzzle file
        with open(puzzleFile, "r") as f:
            # Iterate through each line
            for row, line in enumerate(f):
                tempNumCols = 0
                clean_line = line.rstrip("\n")

                # Then look at each character in each line to determine what that character represents
                for col, char in enumerate(clean_line):
                    if char == "#":
                        self.walls.add((row+1,col+1)) # Wall
                    elif char == '.':
                        self.goals.add((row+1,col+1)) # Goal
                    elif char == '$':
                        boxes.add((row+1,col+1))      # Box 
                    elif char == '@':
                        player = (row+1,col+1)        # Player
                    elif char == '*':                   
                        boxes.add((row+1,col+1))      # Box on a goal will count for both
                        self.goals.add((row+1,col+1))
                    elif char == '+':                
                        player = (row+1,col+1)        # Player on a goal will count for both
                        self.goals.add((row+1,col+1))

                    # Increment the number of columns seen
                    tempNumCols += 1 

                # Increment the number of rows seen and update the number of columns seen if the needed
                numRows += 1
                numCols = max(numCols, tempNumCols)

        # Finally, initialize the height, width, and start State
        self.height = numRows
        self.width = numCols
        self.startState = State(frozenset(boxes), player)
        

    def findDeadlocks(self):
        pass

    def hasReachedGoal(self, state):             
        pass

    def isSpaceReachable(self, state):         
        pass

    def allPushes(self, state):      
        pass

    def applyPush(self, state, box, direction): 
        pass

    def heuristic(self, state):  
        pass

    def printCurrentPuzzle(self, state):        
        pass
