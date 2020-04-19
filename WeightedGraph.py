import random
import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.adj = dict()


class WeightedGraph():
    def __init__(self):
        self.vertices = list()

    def addNode(self, val: str):
        n = Node(val)
        self.vertices.append(n)

    def addWeightedEdge(self, first: Node, second: Node, weight: int):
        if first not in self.vertices or second not in self.vertices:
            print("ERROR: nodes are not in the graph")
            return -1

        # if edge already exists, we do not want to add a duplicate
        if second in first.adj:
            return

        first.adj[second] = weight

    def removeDirectedEdge(self, first: Node, second: Node):
        if first not in self.vertices or second not in self.vertices:
            print("ERROR: nodes are not in the graph")
            return -1

        if second not in first.adj:
            print("ERROR: no edge exists")
            return -1

        del first.adj[second]

    def getNode(self, val: str):
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


def createRandomCompleteWeightedGraph(n: int):
    g = WeightedGraph()

    g.addNode('0')

    for i in range(1, n):
        g.addNode(str(i))

        for j in range(0, i):
            g.addWeightedEdge(g.getNode(str(i)), g.getNode(str(j)), random.randrange(20))
            g.addWeightedEdge(g.getNode(str(j)), g.getNode(str(i)), random.randrange(20))

    return g


def createLinkedList(n: int):
    g = WeightedGraph()

    g.addNode('0')

    for i in range(1, n):
        g.addNode(str(i))
        g.addWeightedEdge(g.getNode(str(i-1)), g.getNode(str(i)), 1)

    return g


def findMin(first: int, second: int):
    if first < second:
        return first
    else:
        return second


def dijkstras(start: Node):
    m = dict()
    output = dict()

    m[start] = 0

    visited = list()
    curr = start

    while curr is not None:
        visited.append(curr)

        for neighbor in curr.adj:
            if neighbor in visited:
                continue

            if neighbor not in m:
                m[neighbor] = sys.maxsize

            m[neighbor] = findMin(m[curr] + curr.adj[neighbor], m[neighbor])

        curr = leastNotVisited(m, visited)

    for node in m:
        output[node.val] = m[node]

    return output


def leastNotVisited(m, visited):
    x = sys.maxsize
    output = None
    for node in m:
        if node in visited:
            output = None
            continue

        if m[node] < x:
            x = m[node]
            output = node

    return output


g = WeightedGraph()

g.addNode('a')
g.addNode('b')
g.addNode('c')
g.addNode('d')
g.addNode('e')
g.addNode('f')
g.addNode('g')

g.addWeightedEdge(g.getNode('a'), g.getNode('b'), 3)
g.addWeightedEdge(g.getNode('b'), g.getNode('a'), 3)

g.addWeightedEdge(g.getNode('a'), g.getNode('c'), 5)
g.addWeightedEdge(g.getNode('c'), g.getNode('a'), 5)

g.addWeightedEdge(g.getNode('a'), g.getNode('d'), 6)
g.addWeightedEdge(g.getNode('d'), g.getNode('a'), 6)

g.addWeightedEdge(g.getNode('b'), g.getNode('d'), 2)
g.addWeightedEdge(g.getNode('d'), g.getNode('b'), 2)

g.addWeightedEdge(g.getNode('c'), g.getNode('d'), 2)
g.addWeightedEdge(g.getNode('d'), g.getNode('c'), 2)

g.addWeightedEdge(g.getNode('c'), g.getNode('f'), 3)
g.addWeightedEdge(g.getNode('f'), g.getNode('c'), 3)

g.addWeightedEdge(g.getNode('c'), g.getNode('g'), 7)
g.addWeightedEdge(g.getNode('g'), g.getNode('c'), 3)

g.addWeightedEdge(g.getNode('d'), g.getNode('f'), 9)
g.addWeightedEdge(g.getNode('f'), g.getNode('d'), 9)

g.addWeightedEdge(g.getNode('f'), g.getNode('e'), 5)
g.addWeightedEdge(g.getNode('e'), g.getNode('f'), 5)

g.addWeightedEdge(g.getNode('f'), g.getNode('g'), 1)
g.addWeightedEdge(g.getNode('g'), g.getNode('f'), 1)

g.addWeightedEdge(g.getNode('c'), g.getNode('e'), 6)
g.addWeightedEdge(g.getNode('e'), g.getNode('c'), 6)

g.addWeightedEdge(g.getNode('e'), g.getNode('g'), 2)
g.addWeightedEdge(g.getNode('g'), g.getNode('e'), 2)

print(dijkstras(g.getNode('a')))
