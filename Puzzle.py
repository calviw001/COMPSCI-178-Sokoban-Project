from pathlib import Path
from State import State
from collections import deque

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

class Puzzle:
    """
    This class will hold all information about a Sokoban puzzle that stays the same. 
    This includes wall positions, goal positions, the height of the puzzle, the width of the puzzle, static deadlock positions,
    and the starting state of the puzzle. 
    """

    def __init__(self, height=0, width=0, walls=set(), goals=set(), start=None):
        self.height = height
        self.width = width
        self.walls = walls
        self.goals = goals
        self.deadlocks = set()        # dead squares, filled by findDeadlocks()
        self.floorSpaces = set()      # walkable squares located within a puzzle, does not count squares outside of walls, 
                                      # filled by findFloorSpaces()
        self.startState = start

    # Read in a Sokoban puzzle in the form of a text file. Parse each line of the file in order to extract the 
    # x and y coordinates of the different Sokoban elements and add that information to the Puzzle class.
    def parsePuzzleFile(self, puzzleFile):
        # Reset the Puzzle on use
        self.walls = set()
        self.goals = set()
        self.deadlocks = set()
        boxes = set()
        player = None

        numRows = 0
        numCols = 0

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

        # Finally, initialize the height, width, start State, and walkable floors
        self.height = numRows
        self.width = numCols
        self.startState = State(frozenset(boxes), player)
        self.findFloorSpaces()

    # Use a BFS to find every walkable square/floor of the Sokoban puzzle.
    # Create a set of these floors and set that equal to 'self.floorSpaces.'
    def findFloorSpaces(self):
        # Create a set to hold the current number of floors discovered
        # Initialize a queue with the player square to start
        currentFloorSpaces = set()
        squareQueue = deque([self.startState.player])

        # Run until the queue is empty
        while squareQueue:
            # Get the first square and its x and y coordinates
            currSquare = squareQueue.popleft()
            currRow, currCol = currSquare

            # Do not add the current square to the queue if its a wall, if its already been added before, or if its located
            # outside the boundaries of the puzzle.
            if currSquare in self.walls or currSquare in currentFloorSpaces:
                continue
            if not (1 <= currRow <= self.height and 1 <= currCol <= self.width):
                continue
            currentFloorSpaces.add(currSquare)

            # Calculate and then add all the neighboring squares to the queue
            for horDir, verDir in DIRECTIONS:
                squareQueue.append((currRow + horDir, currCol + verDir))

        # Once the queue is empty, set 'self.floorSpaces' equal to the set of all floors found
        self.floorSpaces = currentFloorSpaces


    # Use a BFS to find every static deadlock of the Sokoban puzzle.
    # This does not find dynamically created deadlocks that result from getting two or more boxes stuck next to each other.
    def findDeadlocks(self):
        # Initialize a set to hold all non-deadlock squares
        notDeadlocks = set()

        # Initialize a queue with the goal squares to start
        squareQueue = deque()
        for eachGoal in self.goals:
            squareQueue.append(eachGoal)

        # Run until the queue is empty
        while squareQueue:
            # Get the first square and its x and y coordinates
            currSquare = squareQueue.popleft()
            currRow, currCol = currSquare

            # Squares popped from the queue have alright been checked to see if they are non-deadlocks by the for loop later on.
            # Therefore, we can add these squares to our set of non-deadlocks.
            if currSquare in notDeadlocks:
                continue
            notDeadlocks.add(currSquare)

            # For each square, imagine that there is a box on it and a player on one of the box's sides.
            # For each neighboring square, analyze whether a player is able to backtrack and pull a box from the current square to one of 
            # the neighboring squares. 
            for horDir, verDir in DIRECTIONS:
                backTrackedBox = (currRow + horDir, currCol + verDir)
                backTrackedPlayer = (currRow + 2*horDir, currCol + 2*verDir)

                # If a player can indeed pull a box back into a neightboring square, then that square is not a deadlock
                if backTrackedBox in self.floorSpaces and backTrackedPlayer in self.floorSpaces:
                    squareQueue.append(backTrackedBox)

        # Once the queue is empty, set 'self.deadlocks' equal to the set of all floors minus the set of all non-deadlock squares
        self.deadlocks = self.floorSpaces - notDeadlocks


    # Returns true if all of the boxes are on top of a goal and false otherwise.
    def hasReachedGoal(self, state):   
        return self.goals == state.boxes          


    # Use a BFS to find every square that the player of the given state can reach. 
    # Walls and boxes are not reachable because a player can not go inside of a wall or box.
    def allReachableSquares(self, state):         
        # Initialize a set to hold all reachable squares, and a set to hold all seen squares
        # Initialize a queue with the player square to start
        reachableSquares = {state.player}
        squareQueue = deque([state.player])

        # Run until the queue is empty
        while squareQueue:
            # Get the first square and its x and y coordinates
            currSquare = squareQueue.popleft()
            currRow, currCol = currSquare

            # For each neighboring square, check that it can be reached and moved into by a player (not a wall or a box)
            for horDir, verDir in DIRECTIONS:
                neighborSquare = (currRow + horDir, currCol + verDir)

                # Add neighboring square to the queue, and the set of reachable squares if it passes as checks
                if neighborSquare in self.floorSpaces and neighborSquare not in state.boxes and neighborSquare not in reachableSquares:
                    squareQueue.append(neighborSquare)
                    reachableSquares.add(neighborSquare)

        # Once found, return the set of reachable squares
        return reachableSquares

    def allPushes(self, state):      
        pass

    def applyPush(self, state, box, direction): 
        pass

    def heuristic(self, state):  
        pass

    def printCurrentPuzzle(self, state):        
        pass
