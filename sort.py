import random


class Sorting:

    def __init__(self, arr):
        self.arr = arr

    def insertion_sort(self):

        for i in range(1, len(self.arr)):
            card = self.arr[i]
            j = i-1
            while(j >= 0 and self.arr[j] > card):
                self.arr[j+1] = self.arr[j]
                j -= 1
            self.arr[j+1] = card
        return self.arr

    def selection_sort(self):
        for i in range(0, len(self.arr)-1):
            min_val = self.arr[i]
            idx_min = i
            for j in range(i+1, len(self.arr)):
                if(self.arr[j] < min_val):
                    min_val = self.arr[j]
                    idx_min = j

            temp = self.arr[i]
            self.arr[i] = min_val
            self.arr[idx_min] = temp
        return self.arr

    def check_if_numeric(arr):
        try:
            int(arr[0])
            is_numeric = True
        except ValueError:
            is_numeric = False
            return arr

        if(is_numeric):
            arr_num = [0]*len(arr)
            for i in range(len(arr)):
                arr_num[i] = int(arr[i])
        return arr_num

    def bubble_sort(arr):
        # arr = self.check_if_numeric(self.arr)
        for i in range(len(arr), 0, -1):

            for j in range(0, i-1):
                if(arr[j] > arr[j+1]):
                    temp = arr[j+1]
                    arr[j+1] = arr[j]
                    arr[j] = temp
        return arr

    def bucketSort(arr):
        # Assuming arr only contains 0, 1 or 2
        counts = [0, 0, 0]

    # Count the quantity of each val in arr
        for n in arr:
            counts[n] += 1

        # Fill each bucket in the original array
        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                arr[i] = n
                i += 1
        return arr


arr = [0, 2, 1, 2, 0]
print(Sorting.bucketSort(arr))


arr = [5, 2, 4, 6, 1, 3, 4]
arr_strings = ["aa", "a", "a1", "bat", "baa", "ba", "b"]
arr_string_nums = ["5", "1", "11", "3", "03"]
arr_random = [random.randint(0, 100) for i in range(20)]
print(arr_random)
# print(insertion_sort(arr))
# print(selection_sort(arr))
sorting = Sorting(arr)

arr_new = Sorting.check_if_numeric(arr)
# print(arr_new)
# print(Sorting.bubble_sort(arr_new))
