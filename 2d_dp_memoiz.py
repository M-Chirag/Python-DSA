# Count the number of unique paths from the top left to the bottom right of a (m*n) grid.
# You are only allowed to move down or to the right
# [ [0,0,0,0],
#   [0,0,0,0],
#   [0,0,0,0],
#   [0,0,0,0] ]
import time
# brute force approach without DP


def dfs_brute(r, c, rows, cols):

    if r == rows or c == cols:
        return 0
    if r == rows-1 and c == cols-1:
        return 1

    return (dfs_brute(r+1, c, rows, cols) + dfs_brute(r, c+1, rows, cols))


# s_time = time.time()
# print(dfs_brute(0, 0, 10, 10))
# e_time = time.time()

# print(e_time - s_time)


def dfs_dp(r, c, rows, cols, cache):

    if r == rows or c == cols:
        return 0
    if (r, c) in cache:
        return cache[(r, c)]
    if r == rows-1 and c == cols-1:
        return 1

    cache[(r, c)] = dfs_dp(r+1, c, rows, cols, cache) + \
        dfs_dp(r, c+1, rows, cols, cache)
    return cache[(r, c)]


s_time = time.time()
print(dfs_dp(0, 0, 10, 10, {}))
e_time = time.time()

print(e_time - s_time)
