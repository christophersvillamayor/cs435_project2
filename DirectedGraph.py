import random
import math


class Node:
    def __init__(self, val):
        self.val = val
        self.adj = list()
        self.adjLetters = list()


class DirectedGraph:
    def __init__(self):
        self.vertices = list()
        self.letters = list()

    def addNode(self, val):
        n = Node(val)
        self.vertices.append(n)
        self.letters.append(val)

    def addDirectedEdge(self, first: Node, second: Node):
        if first not in self.vertices or second not in self.vertices:
            print("ERROR")
            return -1

        if second in first.adj and second.val in first.adjLetters:
            return

        first.adj.append(second)
        first.adjLetters.append(second.val)

    def removeDirectedEdge(self, first: Node, second: Node):
        if first not in self.vertices or second not in self.vertices:
            print("ERROR")
            return -1

        if second not in first.adj:
            print("ERROR")
            return -1

        first.adj.remove(second)
        first.adjLetters.remove(second.val)

    def getNode(self, val):
        return self.vertices[self.letters.index(val)]

    def getAllNodes(self):
        output = {}
        for n in self.vertices:
            output[n.val] = n.adjLetters

        return output


def createRandomDAGIter(n: int):
    g = DirectedGraph()

    for i in range(0, n):
        g.addNode(str(i))

        if len(g.vertices) > 1:
            g.addDirectedEdge(g.vertices[random.randrange(len(g.vertices)-1)], g.getNode(str(i)))

        if len(g.vertices) > 3:
            small = g.vertices[random.randrange(math.floor(len(g.vertices)/2))]
            large = g.vertices[random.randrange(math.floor(len(g.vertices)/2)) + math.floor(len(g.vertices)/2)]
            g.addDirectedEdge(small, large)

    return g


def Kahns(g: DirectedGraph):
    inDegree = [0]*len(g.vertices)

    for i in range(len(g.vertices)):
        for j in range(len(g.vertices[i].adj)):
            inDegree[g.vertices.index(g.vertices[i].adj[j])] += 1

    q = []
    for i in range(len(inDegree)):
        if inDegree[i] == 0:
            q.append(i)

    count = 0
    order = []

    while q:
        pos = q.pop(0)
        order.append(g.vertices[pos].val)

        for neighbor in g.vertices[pos].adj:
            inDegree[g.vertices.index(neighbor)] -= 1

            if inDegree[g.vertices.index(neighbor)] == 0:
                q.append(g.vertices.index(neighbor))

        count += 1

    if count != len(g.vertices):
        print("There is a cycle")
        return -1

    return order


def mDFS(g: DirectedGraph):
    stack = []
    visited = []

    for n in g.vertices:
        if n not in visited:
            mDFSHelper(n, stack, visited)

    output = []

    while stack:
        output.append(stack.pop())

    return output


def mDFSHelper(n: Node, stack: list, visited: list):
    visited.append(n)
    for neighbor in n.adj:
        if neighbor not in visited:
            mDFSHelper(neighbor, stack, visited)

    stack.append(n.val)


g = createRandomDAGIter(1000)

print(Kahns(g))
print(mDFS(g))
