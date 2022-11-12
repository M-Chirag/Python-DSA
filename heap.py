class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap)-1

        while self.heap[i] < self.heap[i//2]:
            temp = self.heap[i//2]
            self.heap[i//2] = self.heap[i]
            self.heap[i] = temp
            i = i//2

    def pop(self):

        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        # put last element at the root
        self.heap[1] = self.heap.pop()

        i = 1
        while 2*i < len(self.heap):

            # swap with right child
            if (2*i+1 < len(self.heap)) and (self.heap[i] > self.heap[2*i+1]) and (self.heap[2*i+1] < self.heap[2*i]):

                tmp = self.heap[i]
                self.heap[i] = self.heap[2*i+1]
                self.heap[2*i+1] = tmp
                i = 2*i+1

            # swap with left child
            elif (self.heap[i] > self.heap[2*i]):

                tmp = self.heap[i]
                self.heap[i] = self.heap[2*i]
                self.heap[2*i] = tmp
                i = 2*i

            # if there are no swap => it's in the correct place so break the loop
            else:
                break
        return res

    def heapify(self, arr):

        # for n in arr:
        #     self.push(n)

        # move the first element to the end
        arr.append(arr[0])
        self.heap = arr
        self.heap[0] = 0

        curr = (len(self.heap)-1)//2

        while curr > 0:
            i = curr
            # Percolate down
            while 2*i < len(self.heap):  # check if it has left child at least

                # swap with right child
                if (2*i+1 < len(self.heap)) and (self.heap[i] > self.heap[2*i+1]) and (self.heap[2*i+1] < self.heap[2*i]):

                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2*i+1]
                    self.heap[2*i+1] = tmp
                    i = 2*i+1

                # swap with left child
                elif (self.heap[i] > self.heap[2*i]):

                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2*i]
                    self.heap[2*i] = tmp
                    i = 2*i

                # if there are no swap => it's in the correct place so break the loop
                else:
                    break
            curr -= 1


heap = Heap()
arr = [60, 50, 80, 40, 30, 10, 70, 20, 90]
# heap.push(14)
# heap.push(15)
# heap.push(20)
# heap.push(12)
heap.heapify(arr)
print(heap.heap)
# heap.pop()
# print(" after pop")
# print(heap.heap)
