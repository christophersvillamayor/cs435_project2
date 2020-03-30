import random

class Node:
    def __init__(self, val):
        self.val = val
        self.adj = list()
        self.adjLetters = list()


class Graph:
    def __init__(self):
        self.vertices = list()
        self.letters = list()

    def addNode(self, val: str):
        n = Node(val)
        self.vertices.append(n)
        self.letters.append(val)

    def addUndirectedEdge(self, first: Node, second: Node):
        if first in self.vertices:
            first.adj.append(second)
            first.adjLetters.append(second.val)
        else:
            return -1

        if second in self.vertices:
            second.adj.append(first)
            second.adjLetters.append(first.val)
        else:
            return -1

    def removeUndirectedEdge(self, first: Node, second: Node):
        if second in first.adj:
            first.adj.remove(second)
        else:
            return -1

        if first in second.adj:
            second.adj.remove(first)
        else:
            return -1

    def getNode(self, val):
        return self.vertices[self.letters.index(val)]

    def getAllNodes(self):
        output = {}
        for n in self.vertices:
            output[n.val] = n.adjLetters

        return output


def createRandomUnweightedGraphIter(n: int):
    g = Graph()

    for i in range(0, n):
        g.addNode(str(i))

        if len(g.vertices) > 1:
            g.addUndirectedEdge(g.getNode(str(i)), g.vertices[random.randrange(len(g.vertices)-1)])

    return g


def createLinkedList(n: int):
    g = Graph()

    g.addNode(str(0))

    for i in range(1, n):
        g.addNode(str(i))
        g.addUndirectedEdge(g.getNode(str(i)), g.getNode(str(i-1)))

    return g
