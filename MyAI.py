
from AI import AI
from Action import Action


class MyAI( AI ):
    def __init__(self):
        self.board = []
        
    def getAction(self, number: int):
        return