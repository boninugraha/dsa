class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stacks:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def hop(self):
        if self.top is None:
            return None
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
            self.height -= 1
            return temp
    def push(self, value):
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    def print_stacks(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_stacks = Stacks(1)
# my_stacks.push(2)
# my_stacks.push(3)
my_stacks.print_stacks()
print(f"Hop item: {my_stacks.hop()}")
print(f"Hop item: {my_stacks.hop()}")
my_stacks.print_stacks()