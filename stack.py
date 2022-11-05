l = [1, 3, 0, 5, 1, 2, 4]


def indexNextLessRight(l):
    op = []
    stack = []
    for i, e in reversed(list(enumerate(l))):
        while (stack and l[stack[-1]] > e):
            stack.pop()
        op.append(-1) if (not stack) else op.append(stack[-1])
        stack.append(i)
    return op


res = indexNextLessRight(l)
# print(res[::-1])


def indexNextLessLeft(l):
    op = []
    stack = []
    for i, e in enumerate(l):
        while (stack and l[stack[-1]] > e):
            stack.pop()
        op.append(-1) if (not stack) else op.append(stack[-1])
        stack.append(i)
    return op


res2 = indexNextLessLeft(l)
print(res2)
