# Let us implement our own dictionary using a list of linked lists and a hash function
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        if self.head == None:
            self.count = 0
        else:
            self.count = 1

    def __str__(self):
        result = ""
        if self.head == None:
            return result
        cur = self.head
        while cur.next != None:
            result = result + cur.key + ":" + cur.value + " --> "
            cur = cur.next
        result = result + cur.key + ":" + cur.value
        return result

    # insert new node at head of the list
    def insertLL(self, key, value):
        new = Node(key, value)
        new.next = self.head
        self.head = new
        self.count += 1

    # find key in list (return value if found; else return None)
    def findLL(self, key):
        cur = self.head

        while cur != None:
            if cur.key == key:
                return cur.value
            else:
                cur = cur.next
        return None


class Dictionary:
    def __init__(self, size):
        self.buckets = []
        self.size = size
        for i in range(self.size):
            self.buckets.append(LinkedList())

    def __str__(self):
        result = ""
        for i in range(self.size):
            result = result + str(i) + ": " + str(self.buckets[i]) + "\n"
        return result

    def simpleHashFunction(self, key, n):
        assert type(key) == str
        hash_code = 0
        p = 1
        for char in key:
            hash_code += p*ord(char)
            p += 1
        return hash_code % n

    def insert(self, key, value):
        bucket = self.simpleHashFunction(key, self.size)
        self.buckets[bucket].insertLL(key, value)

    def find(self, key):
        bucket = self.simpleHashFunction(key, self.size)
        return self.buckets[bucket].findLL(key)


roster_file = open('roster.csv', 'r')

class_size = 10
load_factor = 0.75
num_buckets = int(class_size/load_factor)

roster2 = Dictionary(num_buckets)

for student in roster_file:
    names = student.strip().split(',')
    roster2.insert(names[0], names[1])

roster_file.close()

print(roster2)
