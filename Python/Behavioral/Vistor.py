class Shape(object):
    def __init__(self):
        raise NotImplementedError

class Dot(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def accept(self, v):
        v.visitDot(self)

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def accept(self, v):
        v.visitCircle(self)

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def accept(self, v):
        v.visitRectangle(self)

class Visitor(object):
    def visitDot(self, dot):
        raise NotImplementedError

    def visitCircle(self, circle):
        raise NotImplementedError

    def visitRectangle(self, rectangle):
        raise NotImplementedError


class XMLVisitor(object):
    def visitDot(self, dot):
        print "dot %s, %s" % (dot.x, dot.y)

    def visitCircle(self, circle):
        print "circle %s, %s, %s" % (circle.x, circle.y, circle.radius)

    def visitRectangle(self, rectangle):
        print "rectangle %s, %s, %s, %s" % (rectangle.x, rectangle.y, rectangle.width, rectangle.height)


all_shape = [Circle(2, 2, 4), Dot(2, 3), Rectangle(2, 2, 3, 4)]
visitor = XMLVisitor()

for shape in all_shape:
    shape.accept(visitor)
