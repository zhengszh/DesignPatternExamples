import math

class RoundHole(object):
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def fits(self, peg):
        print peg.getRadius(), self.getRadius()
        return peg.getRadius() == self.getRadius()

class RoundPeg(object):
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius


class SquarePeg(object):
    def __init__(self, width):
        self.width = width

    def getWidth(self):
        return self.width

class SquarePegAdapter(object):
    def __init__(self, peg):
        self.peg = peg

    def getRadius(self):
        return self.peg.getWidth() * math.sqrt(2) / 2


rp = RoundPeg(1)
rh = RoundHole(1)

sp = SquarePeg(math.sqrt(2))

print rh.fits(rp)
print rh.fits(SquarePegAdapter(sp))
