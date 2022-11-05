# singly linked list class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    # print all elements in a list
    def printList(self):
        cur = self
        while cur != None:
            print(cur.data, end=' ')  # print space-delimited
            cur = cur.next
        print("")  # print final carriage return

    # insert a node after the current node
    def insertAfter(self, node):
        temp = self.next  # current next node
        self.next = node  # set current next to new node
        node.next = temp  # set new node's next to previous next

    # insert a node at the end of the list
    def insertAtEnd(self, node):
        cur = self
        while(cur.next != None):  # iterate through list until last node is found
            cur = cur.next
        cur.insertAfter(node)  # insert node

    def insertAtIndex(self, node, index):
        cur = self
        count = 0
        while(cur.next != None and count < index):
            cur = cur.next
            count += 1
        cur.insertAfter(node)


# driver code for testing insertAfter
head = Node("A")
head.insertAfter(Node("B"))
head.insertAfter(Node("C"))
head.printList()

# driver code for testing insertAtEnd
# head = Node("A")
# head.insertAtEnd(Node("B"))
# head.insertAtEnd(Node("C"))
# head.insertAtEnd(Node("D"))
# head.insertAtEnd(Node("E"))
# head.printList()
