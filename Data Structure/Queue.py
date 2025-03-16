class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def dequeue(self):
        if self.first is None:
            return None
        else:
            temp = self.first
            self.first = temp.next
            temp.next = None
            self.length -= 1
            return temp
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
my_queue = Queue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.print_queue()
print("AFTER")
print(f"DEQUEUE: {my_queue.dequeue().value}")
print(f"DEQUEUE: {my_queue.dequeue().value}")
print(f"DEQUEUE: {my_queue.dequeue().value}")
print(f"DEQUEUE: {my_queue.dequeue()}")
my_queue.print_queue()
