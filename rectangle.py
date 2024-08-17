
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setX(self, value):
        if value >= 0:
            self.x = value
            return True
        else:
            return False

    def setY(self, value):
        if value >= 0:
            self.y = value
            return True
        else:
            return False

    def setWidth(self, value):
        if value >= 0:
            self.width = value
            return True
        else:
            return False

    def setHeight(self, value):
        if value >= 0:
            self.height = value
            return True
        else:
            return False
    def getArea(self):
        Area = self.width * self.height

        return Area
    def getPerimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter
