class Shape(object):
    def draw(self):
        raise NotImplementedError

class Rectangle(Shape):
    def draw(self):
        print "Draw Rectangle"

class Circle(Shape):
    def draw(self):
        print "Draw Circle"

class ShapeDecorator(Shape):
    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        self.shape.draw()

class RedShapeDecorator(ShapeDecorator):
    def draw(self):
        self.shape.draw()
        self.setRedBorder()

    def setRedBorder(self):
        print "Border:Red"

circle = Circle()
redCircle = RedShapeDecorator(Circle())
redRectangle = RedShapeDecorator(Rectangle())

circle.draw()
redCircle.draw()
redRectangle.draw()
