# find number of set bits

def setBits(n):

    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1
    return count


print(setBits(27))
