class Action():
    def _init_(self, action, x, y):
        self._action = action
        self._x = x
        self._y = y

    def getMove(self):
        return self._action
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y