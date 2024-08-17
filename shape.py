class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    def setX(self, value):
        if isinstance(value, (int, float)):
            self.x = value
            return True
        else:
            return False

    def setY(self, value):
        if isinstance(value, (int, float)):
            self.y = value
            return True
        else:
            return False