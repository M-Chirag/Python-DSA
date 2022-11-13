from collections import deque
# Find the length of the shortest path from the top left of the grid to the bottom right


def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])

    visit = set()
    queue = deque()

    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS-1 and c == COLS-1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                new_r, new_c = r+dr, c+dc

                if (min(new_c, new_r) < 0 or new_r == ROWS or new_c == COLS or
                        (new_r, new_c) in visit or grid[new_r][new_c] == 1):
                    continue
                queue.append((new_r, new_c))
                visit.add((new_r, new_c))
        length += 1


grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

print(bfs(grid))
