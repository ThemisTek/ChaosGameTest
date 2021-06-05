
from enum import Enum 

class Point:
    def __init__(self):
        pass

class Point:
    def __init__(self,x : float,y : float):
        self.x = x
        self.y = y
    @staticmethod
    def Between(fromPoint : Point ,toPoint: Point):
        distX = fromPoint.x + (toPoint.x - fromPoint.x)/2
        distY = fromPoint.y + (toPoint.y - fromPoint.y)/2
        return Point(distX,distY)
    def Copy(self):
        return Point(self.x,self.y)


class Triangle:
    def __init__(self,a : Point, b: Point , c: Point):
        self.a = a
        self.b = b
        self.c = c
