class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertatbeg(self,data):
        node = Node(data, self.head)
        self.head = node

    def printlinkedlist(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        ll = []
        while itr:
            ll.append(itr.data)
            itr = itr.next
        print(ll)
    def insetatend(self,data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
if __name__ == '__main__':
    lnk= Linkedlist()
    lnk.insertatbeg(5)
    lnk.insertatbeg(10)
    lnk.insertatbeg(15)
    lnk.insertatbeg(12)
    lnk.printlinkedlist()



