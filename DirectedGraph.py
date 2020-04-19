import random
import math


class Node:
    def __init__(self, val):
        self.val = val
        self.adj = list()


class DirectedGraph:
    def __init__(self):
        self.vertices = list()

    def addNode(self, val):
        n = Node(val)
        self.vertices.append(n)

    def addDirectedEdge(self, first: Node, second: Node):
        if first not in self.vertices or second not in self.vertices:
            print("ERROR: nodes are not part of the graph")
            return -1

        # If edge already exists we don't want to append another to neighbors
        if second in first.adj:
            return

        first.adj.append(second)

    def removeDirectedEdge(self, first: Node, second: Node):
        if first not in self.vertices or second not in self.vertices:
            print("ERROR: nodes are not part of the graph")
            return -1

        if second not in first.adj:
            print("ERROR: nodes do not have an existing edge")
            return -1

        first.adj.remove(second)

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


def createRandomDAGIter(n: int):
    g = DirectedGraph()

    for i in range(0, n):
        g.addNode(str(i))

        # When we have more than 1 node, add a directed edge from a random node (0 to n-1) to n
        if len(g.vertices) > 1:
            g.addDirectedEdge(g.vertices[random.randrange(len(g.vertices)-1)], g.getNode(str(i)))

        # When we have more than 3 nodes, choose a random node in the first half of vertices list
        # and choose a random node in the last half of the vertices list
        # create a directed edge from the first half node to the last half node
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

    queue = []
    for i in range(len(inDegree)):
        if inDegree[i] == 0:
            queue.append(i)

    count = 0
    order = []

    while queue:
        pos = queue.pop(0)
        order.append(g.vertices[pos].val)

        for neighbor in g.vertices[pos].adj:
            inDegree[g.vertices.index(neighbor)] -= 1

            if inDegree[g.vertices.index(neighbor)] == 0:
                queue.append(g.vertices.index(neighbor))

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
