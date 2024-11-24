class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        lltr = ''
        curr_head = self.head
        while curr_head is not None:
            lltr += str(curr_head.data) + ' --> '
            curr_head = curr_head.next
        print(lltr)

l1= LinkedList()
l1.insert_at_beginning(4)
l1.insert_at_beginning(64)
l1.print()