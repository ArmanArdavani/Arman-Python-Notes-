from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1==p2)

# If your class has no methods and it only contain data (attrubutes),
# use a namedtuple isntead. 