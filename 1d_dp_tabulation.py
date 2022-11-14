def fib(n):

    if n <= 1:
        return n
    dp = [0, 1]  # optimized for memory, we can also create dp array of len equal to n
    i = 2
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0]+dp[1]
        dp[0] = tmp
        i += 1
    return dp[1]


print(fib(20))
