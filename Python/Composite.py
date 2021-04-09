class Graphic(object):
    def move(self, x, y):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

class Dot(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def draw(self):
        print "Draw Dot: %s, %s" % (self.x, self.y)


class Circle(Dot):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        print "Draw Circle: %s, %s, %s" % (self.x, self.y, self.radius)


class CompoundGraphic(Graphic):
    def __init__(self):
        self.children = []

    def move(self, x, y):
        for child in self.children:
            child.move(x, y)

    def draw(self):
        for child in self.children:
            child.draw()
        print "=================="

    def add(self, child):
        if child in self.children:
            return
        self.children.append(child)

    def remove(self, child):
        if child not in self.children:
            return
        self.children.remove(child)


graph = CompoundGraphic()
graph.add(Dot(1, 2))
graph.add(Circle(5, 3, 10))
sub_graph = CompoundGraphic()
sub_graph.add(Circle(4, 4, 1))
graph.add(sub_graph)

graph.draw()

graph.move(4, 6)
graph.draw()

graph.remove(sub_graph)

graph.draw()
