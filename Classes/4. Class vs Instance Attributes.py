class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x 
        self.y = y 
        
    def draw(self):
        print(f"Point({self.x}, {self.y})")


point = Point(2, 4)
print(point.default_color)
print(Point.default_color)
point.draw()

Point.color_2 = "Yellow"
point_2 = Point(3,7)
print(Point.color_2)
print(point_2.color_2)
point_2.draw()