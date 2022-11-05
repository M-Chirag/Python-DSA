def seats_allocation(arr):
    q = []
    res = [0 for i in range(len(arr)+1)]
    for i in range(1, len(arr)+1):
        q.append((i, arr[i-1]))

    while q:
        if(res[q[0][1]] == 0):
            res[q[0][1]] = q[0]
            q.pop(0)
        else:
            ind, val = q.pop(0)
            q.append((ind, val+1))
    res.pop(0)
    ans = [v for i, v in sorted(res)]
    return ans


arr = [1, 3, 3, 2, 2]
print(seats_allocation(arr))
