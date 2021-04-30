class Image(object):
    def display(self):
        raise NotImplementedError

class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load(filename)

    def load(self, filename):
        print "Loading %s" % filename

    def display(self):
        print "display %s" % self.filename

class ProxyImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.realImage = None

    def display(self):
        if not self.realImage:
            self.realImage = RealImage(self.filename)
        self.realImage.display()

image = ProxyImage("test.jpg")
image.display()
image.display()
