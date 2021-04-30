class TreeType(object):
    def __init__(self, color):
        print "Create tree: %s" % color
        self.color = color

    def draw(self, x, y):
        print "Draw Tree in %s, %s, %s" % (x, y, self.color)

class TreeFactory(object):
    TREE_TYPES = {}

    @classmethod
    def getTreeType(self, color):
        ttype = self.TREE_TYPES.get(color)
        if not ttype:
            ttype = TreeType(color)
            self.TREE_TYPES[color] = ttype
        return ttype

class Tree(object):
    def __init__(self, x, y, ttype):
        self.x = x
        self.y = y
        self.type = ttype

    def draw(self):
        self.type.draw(self.x, self.y)

class Forrest(object):
    def __init__(self):
        self.trees = []

    def plantTree(self, x, y, color):
        ttype = TreeFactory.getTreeType(color)
        tree = Tree(x, y, ttype)
        self.trees.append(tree)

    def draw(self):
        for tree in self.trees:
            tree.draw()

forrest = Forrest()
forrest.plantTree(1, 1, "Red")
forrest.plantTree(2, 1, "Green")
forrest.plantTree(4, 4, "Red")
forrest.draw()
