# Count the number of unique paths from the top left to the bottom right of a (m*n) grid.
# You are only allowed to move down or to the right
# [ [0,0,0,0],
#   [0,0,0,0],
#   [0,0,0,0],
#   [0,0,0,0] ]


def dp_bottom_up(rows, cols):

    # initially set, can be considered as extra list that provides 0's
    prevRow = [0]*cols

    for r in range(rows-1, -1, -1):
        curRow = [0]*cols
        curRow[cols-1] = 1  # initializing the last column values to 1
        for c in range(cols-2, -1, -1):
            curRow[c] = curRow[c+1] + prevRow[c]
        prevRow = curRow

    return prevRow[0]


print(dp_bottom_up(10, 10))
