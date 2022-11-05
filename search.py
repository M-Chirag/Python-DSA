import random


class Search:
    # def __init__(self, arr):
    #     self.arr = arr

    def binary_search_iterative(self, arr, target):
        if not arr:
            return None
        l, r = 0, len(arr)
        while l < r:
            m = (l+r)//2
            if(arr[m] == target):
                return m
            if(arr[m] < target):
                l = m+1
            if(arr[m] > target):
                r = m-1
        return None

    def binary_search_recursive(self, arr, target, l, r):
        m = (l+r)//2
        if(l > r):
            return
        else:
            if(arr[m] == target):
                return m
            elif(arr[m] < target):
                return self.binary_search_recursive(arr, target, m+1, r)
            elif(arr[m] > target):
                return self.binary_search_recursive(arr, target, l, m-1)


searching = Search()
# the_list = [27, 78, 105, 135, 411, 431, 434,
#             468, 493, 501, 525, 534, 551, 654, 780]
# print(searching.binary_search_recursive(the_list, 493, 0, len(the_list)-1))

N = int(input("Please enter the number of elements(N) in the list: "))
the_list = [random.randint(0, 1000) for i in range(N)]
print("Your generated list is: ", sorted(the_list))
while True:
    query = input("Enter the number to be searched in this list \n" +
                  "OR Enter '?' to print the list \n" +
                  "OR Enter 'q' to quit: \n")
    if(query == '?'):
        print(sorted(the_list))
    elif(query == 'q'):
        break
    else:
        num = int(query)
        print(num)
        print(searching.binary_search_recursive(
            sorted(the_list), num, 0, N-1))
