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
    elif len(n.adj) == 0:
        return

    for neighbor in n.adj:
        if neighbor not in visited:
            DFSRecHelper(neighbor, end, visited, output)


def DFSIter(start: Graph.Node, end: Graph.Node):
    output = [start.val]
    visited = [start]
    stack = [start]

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
    queue = []
    visited = []
    output = []

    for n in g.vertices:
        if n not in visited:
            queue.append(n)
            BFSRecHelper(queue, visited, output)

    return output


def BFSRecHelper(queue, visited, output):
    if len(queue) == 0:
        return

    curr = queue.pop(0)

    for neighbor in curr.adj:
        if neighbor not in visited:
            visited.append(neighbor)
            output.append(neighbor.val)
            queue.append(neighbor)

    BFSRecHelper(queue, visited, output)


def BFSIter(g: Graph.Graph):
    output = []
    visited = []
    queue = []

    # iterate through g.vertices
    for n in g.vertices:
        # add current node to visited
        # add the node's val to output
        # and add the node to the queue
        if n not in visited:
            visited.append(n)
            output.append(n.val)
            queue.append(n)

            # While the queue is not empty
            while len(queue) > 0:
                # cur = first node in list
                cur = queue.pop(0)

                # iterate through neighbors of cur
                for neighbor in cur.adj:

                    # add current node to visited
                    # add the node's val to output
                    # and add the node to the queue
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
