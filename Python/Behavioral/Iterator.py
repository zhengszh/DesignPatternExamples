
class Iterator(object):
    def hasNext(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

class Tree(object):
    def getBfsIterator(self):
        raise NotImplementedError

    def getDfsIterator(self):
        raise NotImplementedError

class ConcreteTree(Tree):
    class ConcreteTreeNode(object):
        def __init__(self, val):
            self.children = []
            self.value = val

        def __str__(self):
            child_str = []
            for child in self.children:
                child_str.append(child.__str__())
            return "%s, [%s]" % (self.value, ",".join(child_str))

    def __init__(self, values):
        self.root = None
        if not values:
            return
        self.root = self.Build(values, 0)

    def Build(self, values, idx):
        if idx >= len(values):
            return None
        node = self.ConcreteTreeNode(values[idx])
        for off in xrange(1, 3):
            i = idx * 2 + off
            if i >= len(values):
                continue
            child = self.Build(values, i)
            child and node.children.append(child)
        return node

    def getBfsIterator(self):
        return self.BfsIterator(self)

    def getDfsIterator(self):
        return self.DfsIterator(self)

    class BfsIterator(Iterator):
        def __init__(self, tree):
            self.bfs_queue = []
            if tree.root:
                self.bfs_queue.append(tree.root)

        def hasNext(self):
            return bool(self.bfs_queue)

        def next(self):
            if not self.bfs_queue:
                return None
            front = self.bfs_queue[0]
            res = front.value
            for child in front.children:
                self.bfs_queue.append(child)
            self.bfs_queue = self.bfs_queue[1:]
            return res

    class DfsIterator(Iterator):
        def __init__(self, tree):
            self.dfs_stack = []
            if tree.root:
                self.dfs_stack.append(tree.root)

        def hasNext(self):
            return bool(self.dfs_stack)

        def next(self):
            if not self.dfs_stack:
                return None
            front = self.dfs_stack[-1]
            self.dfs_stack.pop(-1)
            res = front.value
            for child in reversed(front.children):
                self.dfs_stack.append(child)
            return res

tree = ConcreteTree([1,2,3,4,5,6,7])
print tree.root
it = tree.getBfsIterator()
print "bfs:"
while it.hasNext():
    print it.next()

it = tree.getDfsIterator()
print "dfs:"
while it.hasNext():
    print it.next()

