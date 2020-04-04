import random
import sys


class GridNode:
    def __init__(self, x: int, y: int, val: str):
        self.x = x
        self.y = y
        self.val = val
        self.adj = list()
        self.adjLetters = list()


class GridGraph:
    def __init__(self):
        self.vertices = list()
        self.letters = list()
        self.coordinates = list()

    def addGridNode(self, x: int, y: int, val: str):
        if (x, y) in self.coordinates:
            print("Already exists " + val)
            return -1

        n = GridNode(x, y, val)
        self.vertices.append(n)
        self.letters.append(val)
        self.coordinates.append((x, y))

    def addUndirectedEdge(self, first: GridNode, second: GridNode):
        if abs(first.x - second.x) > 1 or abs(first.y - second.y) > 1:
            print("ERROR")
            return -1

        if first not in self.vertices or second not in self.vertices:
            print("ERROR")
            return -1

        first.adj.append(second)
        second.adj.append(first)

        first.adjLetters.append(second.val)
        second.adjLetters.append(first.val)

    def removeUndirectedEdge(self, first: GridNode, second: GridNode):
        if first not in self.vertices or second not in self.vertices:
            print("ERROR")
            return -1

        if second in first.adj:
            first.adj.remove(second)
            first.adjLetters.remove(second.val)
        else:
            print("ERROR")
            return -1

        if first in second.adj:
            second.adj.remove(first)
            second.adjLetters.remove(first.val)
        else:
            print("ERROR")
            return -1

    def getNode(self, val):
        return self.vertices[self.letters.index(val)]

    def getAllNodes(self):
        output = dict()

        for n in self.vertices:
            output[n.val] = n.adjLetters

        return output


def createRandomGridGraph(n: int):
    g = GridGraph()

    # Create first row with chance of each node being neighbors
    for i in range(n):
        g.addGridNode(i, 0, str(i) + ", 0")

        if i > 0:
            chance = random.randrange(2)
            if chance == 1:
                g.addUndirectedEdge(g.getNode(str(i) + ", 0"), g.getNode(str(i-1) + ", 0"))

    # Create rest of graph with chance of nodes above and next to it being neighbors
    for i in range(1, n):
        for j in range(0, n):
            g.addGridNode(j, i, str(j) + ", " + str(i))

            chance = random.randrange(2)
            if chance == 1:
                g.addUndirectedEdge(g.getNode(str(j) + ", " + str(i)), g.getNode(str(j) + ", " + str(i-1)))

            if j > 0:
                chanceNext = random.randrange(2)
                if chanceNext == 1:
                    g.addUndirectedEdge(g.getNode(str(j) + ", " + str(i)), g.getNode(str(j-1) + ", " + str(i)))

    return g


def astar(src: GridNode, dst: GridNode):
    m = dict()
    p = dict()
    output = list()
    visited = list()

    h = abs(dst.x - src.x) + abs(dst.y + src.y)
    m[src] = (0, h)
    curr = src

    while curr is not dst:
        visited.append(curr)
        for neighbor in curr.adj:
            if neighbor not in visited:
                g = abs(neighbor.x - src.x) + abs(neighbor.y - src.y)
                h = abs(dst.x - neighbor.x) + abs(dst.y - neighbor.y)

            if neighbor in m:
                if g < m[neighbor][0]:
                    m[neighbor] = (g, h)
            else:
                m[neighbor] = (g, h)
                p[neighbor] = curr

        small = sys.maxsize
        for n in m:
            if n in visited:
                continue
            if m[n][0] + m[n][1] < small:
                small = m[n][0] + m[n][1]
                curr = n

        if small == sys.maxsize:
            print("NO SOLUTION")
            return -1

    while curr is not src:
        output.insert(0, curr.val)
        curr = p[curr]
    output.insert(0, src.val)

    return output


# 100x100 maze
# Solution not guaranteed from (0,0) to (99,99) since whole graph is random

maze = createRandomGridGraph(100)
print(astar(maze.getNode("0, 0"), maze.getNode("99, 99")))


# example with a solution

print()
g = GridGraph()

for y in range(0, 5):
    for x in range(0, 5):
        g.addGridNode(x, y, str(x) + str(y))

g.addUndirectedEdge(g.getNode('00'), g.getNode('10'))
g.addUndirectedEdge(g.getNode('10'), g.getNode('11'))
g.addUndirectedEdge(g.getNode('10'), g.getNode('20'))
g.addUndirectedEdge(g.getNode('20'), g.getNode('30'))
g.addUndirectedEdge(g.getNode('30'), g.getNode('40'))

g.addUndirectedEdge(g.getNode('01'), g.getNode('11'))
g.addUndirectedEdge(g.getNode('11'), g.getNode('21'))
g.addUndirectedEdge(g.getNode('11'), g.getNode('12'))
g.addUndirectedEdge(g.getNode('21'), g.getNode('31'))
g.addUndirectedEdge(g.getNode('31'), g.getNode('32'))
g.addUndirectedEdge(g.getNode('31'), g.getNode('41'))
g.addUndirectedEdge(g.getNode('41'), g.getNode('42'))

g.addUndirectedEdge(g.getNode('02'), g.getNode('12'))
g.addUndirectedEdge(g.getNode('12'), g.getNode('22'))
g.addUndirectedEdge(g.getNode('32'), g.getNode('33'))

g.addUndirectedEdge(g.getNode('03'), g.getNode('13'))
g.addUndirectedEdge(g.getNode('03'), g.getNode('04'))
g.addUndirectedEdge(g.getNode('13'), g.getNode('14'))
g.addUndirectedEdge(g.getNode('23'), g.getNode('33'))
g.addUndirectedEdge(g.getNode('33'), g.getNode('43'))
g.addUndirectedEdge(g.getNode('43'), g.getNode('44'))

g.addUndirectedEdge(g.getNode('24'), g.getNode('34'))
g.addUndirectedEdge(g.getNode('34'), g.getNode('44'))

print(g.getAllNodes())
print(astar(g.getNode('00'), g.getNode('44')))