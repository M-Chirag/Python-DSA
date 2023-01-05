# Brute Force approach
# TC = O(2^n) SC = O(n)
def dfs(profit, weight, capacity):
    return dfsHelper(0, profit, weight, capacity)


def dfsHelper(i, profit, weight, capacity):

    if i == len(profit):
        return 0

    # skip the item
    maxProfit = dfsHelper(i+1, profit, weight, capacity)

    # include the item
    newCap = capacity - weight[i]

    if newCap >= 0:
        p = profit[i]+dfsHelper(i+1, profit, weight, newCap)

        maxProfit = max(maxProfit, p)

    return maxProfit

# Memoization solution
# TC = O(n*m) SC = O(n*m) n-> number of items, m -> capacity


def memo(profit, weight, capacity):
    N, M = len(profit), capacity
    cache = [[-1] * (M+1) for _ in range(N)]
    return memoHelper(0, profit, weight, capacity, cache)


def memoHelper(i, profit, weight, capacity, cache):

    if i == len(profit):
        return 0
    if cache[i][capacity] != -1:
        return cache[i][capacity]

    # skip the item
    cache[i][capacity] = memoHelper(i+1, profit, weight, capacity, cache)

    # include the item
    newCap = capacity-weight[i]

    if newCap >= 0:
        p = profit[i]+memoHelper(i+1, profit, weight, newCap, cache)

        cache[i][capacity] = max(p, cache[i][capacity])

    return cache[i][capacity]

# Bottom Up true DP solution
# TC = O(n*m), SC = O(n*m)


def dp(profit, weight, capacity):

    N, M = len(profit), capacity
    dp = [[0]*(M+1) for _ in range(N)]

    # Fill the first row and column to handle edge cases
    for i in range(N):
        dp[i][0] = 0
    for c in range(M+1):
        if weight[0] <= c:
            dp[0][c] = profit[0]

    # Iterate over all cells starting from the 2nd row and column, each cell represents maxProfit possible at the
    # column (capacity) and all items at and before the current item
    for i in range(1, N):
        for c in range(1, M+1):

            # if we skip just take value at same capacity and previous item
            skip = dp[i-1][c]
            include = 0
            newCap = c-weight[i]  # find newCap if we include it
            if newCap >= 0:
                # calculate new profit by adding curr item profit and maxProfit with new cap
                include = profit[i]+dp[i-1][newCap]
            dp[i][c] = max(skip, include)  # save the maxProfit in the dp
    # print(dp)
    return dp[N-1][M]

# Space optimized DP solution as we only need 2 rows at any given time
# TC = O(m*n) SC = O(2*m)= O(m)


def dpSpaceOptimized(profit, weight, capacity):

    N, M = len(profit), capacity
    dp = [0]*(M+1)

    for i in range(N):
        curRow = [0]*(M+1)
        for c in range(1, M+1):

            skip = dp[c]

            include = 0
            newCap = c-weight[i]
            if newCap >= 0:
                include = profit[i]+dp[newCap]

            curRow[c] = max(include, skip)
        dp = curRow
    return dp[M]


profit = [4, 4, 7, 1]
weight = [5, 2, 3, 1]
capacity = 8

# print(dfs(profit, weight, capacity))
# print(memo(profit, weight, capacity))
# print(dp(profit, weight, capacity))
print(dpSpaceOptimized(profit, weight, capacity))
