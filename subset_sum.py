def memoiz(target, i, nums, dp):

    if dp[i][target] != 0:
        return dp[i][target]
    # print(sum)
    if target == 0:
        print("reached")
        return 1
    if i == 0:
        return 0

    skip = memoiz(target, i-1, nums, dp)
    include = 0
    newSum = target-nums[i-1]
    if newSum >= 0:
        include = memoiz(newSum, i-1, nums, dp)

    dp[i][target] = (skip + include)
    return dp[i][target]


nums = [2, 3, 7, 10]
N, M = len(nums), 12
dp = [[0]*(M+1) for _ in range(N+1)]
print(memoiz(M, N, nums, dp))
print(dp)
