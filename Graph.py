import random


class Node:
    def __init__(self, val):
        self.val = val
        self.adj = list()


class Graph:
    def __init__(self):
        self.vertices = list()

    def addNode(self, val: str):
        n = Node(val)
        self.vertices.append(n)

    def addUndirectedEdge(self, first: Node, second: Node):
        if first in self.vertices:
            first.adj.append(second)
        else:
            print("ERROR: node " + first.val + " is not in the graph")
            return -1

        if second in self.vertices:
            second.adj.append(first)
        else:
            print("ERROR: node " + second.val + " is not in the graph")
            return -1

    def removeUndirectedEdge(self, first: Node, second: Node):
        if first not in self.vertices or second not in self.vertices:
            print("ERROR: given nodes are not in the graph")
            return -1

        if second in first.adj:
            first.adj.remove(second)

        if first in second.adj:
            second.adj.remove(first)

    def getNode(self, val):
        for node in self.vertices:
            if node.val == val:
                return node

    def getAllNodes(self):
        output = dict()

        for node in self.vertices:
            output[node.val] = list()
            for neighbor in node.adj:
                output[node.val].append(neighbor.val)

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
        nextNode = Node(str(i))
        g.vertices.append(nextNode)
        g.vertices[i-1].adj.append(nextNode)

    return g


g = createLinkedList(5)
print(g.getAllNodes())
