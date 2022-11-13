from collections import deque
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


def bfs(node, target, adjList):

    q = deque()
    visit = set()

    q.append(node)
    visit.add(node)
    length = 0

    while q:
        for i in range(len(q)):
            curr = q.popleft()

            if curr == target:
                return length

            for neighbor in adjList[node]:

                if neighbor not in visit:
                    q.append(neighbor)
                    visit.add(neighbor)
        length += 1
    return length


edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
adjList = buildAdjList(edges)

print(adjList)

curr_time = time.time()
print(bfs("A", "E", adjList))
end_time = time.time()

print(end_time-curr_time)
