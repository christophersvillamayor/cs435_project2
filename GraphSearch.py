import Graph


def DFSRec(start: Graph.Node, end: Graph.Node):
    visited = []
    output = []

    DFSRecHelper(start, end, visited, output)
    return output


def DFSRecHelper(n: Graph.Node, end: Graph.Node, visited, output):
    if len(visited) != 0:
        if visited[-1] == end:
            return

    if n is None:
        return

    visited.append(n)
    output.append(n.val)

    if n == end:
        return

    if len(n.adj) == 0:
        return

    for neighbor in n.adj:
        if neighbor not in visited:
            DFSRecHelper(neighbor, end, visited, output)


def DFSIter(start: Graph.Node, end: Graph.Node):
    output = []
    visited = []
    stack = []

    output.append(start.val)
    visited.append(start)
    stack.append(start)

    while len(stack) > 0:
        cur = stack.pop()

        if cur == end:
            return output
        for neighbor in cur.adj:
            if neighbor not in visited:
                output.append(neighbor.val)
                visited.append(neighbor)
                stack.append(neighbor)

    return None


def BFSRec(g: Graph.Graph):
    q = []
    visited = []
    output = []

    for n in g.vertices:
        if n not in visited:
            q.append(n)
            BFSRecHelper(q, visited, output)

    return output


def BFSRecHelper(q, visited, output):
    if len(q) == 0:
        return

    curr = q.pop(0)

    for neighbor in curr.adj:
        if neighbor not in visited:
            visited.append(neighbor)
            output.append(neighbor.val)
            q.append(neighbor)

    BFSRecHelper(q, visited, output)


def BFSIter(g: Graph.Graph):
    output = []
    visited = []
    queue = []

    for n in g.vertices:
        if n not in visited:
            visited.append(n)
            output.append(n.val)
            queue.append(n)
            while len(queue) > 0:
                cur = queue.pop(0)
                for neighbor in cur.adj:
                    if neighbor not in visited:
                        output.append(neighbor.val)
                        visited.append(neighbor)
                        queue.append(neighbor)

    return output


def BFSRecLinkedList(g: Graph.Graph):
    print(BFSRec(g))


def BFSIterLinkedList(g: Graph.Graph):
    print(BFSIter(g))


g = Graph.createRandomUnweightedGraphIter(5)

print(g.getAllNodes())
print(BFSRec(g))