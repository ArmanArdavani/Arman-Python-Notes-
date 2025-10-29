class Point:
    def draw(self):
        print("Draw")


point = Point()
print(type(point))

print(isinstance(point, Point))  # point is an instanse of the Point Class 
print(isinstance(point, int))    # Point is not an instance of the int Class 