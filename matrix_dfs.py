# Find the number of unique paths from the top left element to the bottom right element in a matrix (grid)
# You can only count the path with 0's

def dfs(grid, r, c, visit):

    ROWS, COLS = len(grid), len(grid[0])

    if (min(r, c) < 0 or (r, c) in visit or
            r == ROWS or c == COLS or grid[r][c] == 1):
        return 0

    if (r == ROWS-1) and (c == COLS-1):
        return 1

    visit.add((r, c))

    count = 0
    count += dfs(grid, r+1, c, visit)
    count += dfs(grid, r-1, c, visit)
    count += dfs(grid, r, c+1, visit)
    count += dfs(grid, r, c-1, visit)

    visit.remove((r, c))

    return count


grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

print(dfs(grid, 0, 0, set()))
