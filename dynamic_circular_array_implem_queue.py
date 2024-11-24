class Queue_dyn(object):
    def __init__(self, limit = 5):
        self.que = []
        self.front = None
        self.rear = None
        self.limit = limit
        self.size = 0

    def isEmpty(self):
        return self.size <= 0

    def enQueue(self, item):
        if self.size >= self.limit:
            self.resize()
        self.que.append(item)
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1
        print("Queue after enQueue: ", self.que)

    def deQueue(self):
        if self.size <= 0:
            print('Queue Underflow')
            return 0
        else:
            self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1

        print("Queue after deQueue: ", self.que)

    def queueRear(self):
        if self.rear is None:
            print("Queue is empty! ")
            raise IndexError
        else:
            return self.que[self.rear]

    def queueFront(self):
        if self.front is None:
            print("Queue is empty! ")
            raise IndexError
        else:
            return self.que[self.front]

    def size(self):
        return self.size

    def resize(self):
        newQue = list(self.que)
        self.limit = 2 * self.limit
        self.que = newQue

que = Queue_dyn()
que.enQueue("First")
que.queueFront()
que.queueRear()
que.enQueue("Second")
que.queueFront()
que.queueRear()
que.enQueue("Third")
que.queueFront()
que.queueRear()
que.enQueue("Forth")
que.queueFront()
que.queueRear()
que.enQueue("Fifth")
que.queueFront()
que.queueRear()
que.enQueue("Sixth")
que.queueFront()
que.queueRear()
que.enQueue("Seventh")
que.queueFront()
que.queueRear()
que.enQueue("Eight")
que.queueFront()
que.queueRear()
que.enQueue("Ninth")
que.deQueue()
que.queueFront()
que.queueRear()
que.deQueue()
que.queueFront()
que.queueRear()
que.deQueue()
que.queueFront()
que.queueRear()


