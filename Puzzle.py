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

    def parsePuzzleFile(self, puzzleFile):
        pass

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
