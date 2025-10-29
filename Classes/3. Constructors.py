class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        
    def draw(self):
        print(f"Point({self.x}, {self.y})")

point = Point(2,4)
print(point.x)
print(point.y)
point.draw()