# Find a non-empty subarray with the largest sum

# brute force approach
def naive(nums):
    maxSum = nums[0]
    for i in range(len(nums)):
        curSum = 0
        for j in range(i, len(nums)):
            curSum += nums[j]
            maxSum = max(maxSum, curSum)
    return maxSum


def kadanes(nums):
    maxSum = nums[0]
    currSum = 0
    maxL, maxR = 0, 0

    l, r = 0, 0
    while r < len(nums):
        if (nums[r] > (currSum+nums[r])):
            l = r
            currSum = nums[r]
        else:
            currSum += nums[r]

        if currSum > maxSum:
            maxSum = currSum
            maxL, maxR = l, r
        r += 1

    return (maxSum, maxL, maxR)


arr = [4, -1, 2, -7, 3, 4]
print(kadanes(arr))
