import time


def buildAdjList(edges):

    adjList = {}

    for src, dst in edges:
        if src not in adjList:
            adjList[src] = []
        if dst not in adjList:
            adjList[dst] = []
        adjList[src].append(dst)
    return adjList


def dfs(node, target, adjList, visit):

    if node in visit:
        return 0
    if node == target:
        return 1
    visit.add(node)
    count = 0
    for neighbor in adjList[node]:

        count += dfs(neighbor, target, adjList, visit)

    visit.remove(node)
    return count


edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
adjList = buildAdjList(edges)

print(adjList)

curr_time = time.time()
print(dfs("A", "E", adjList, set()))

end_time = time.time()

print(end_time-curr_time)
