class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)

        if new_node is None:
            self.head = new_node
            self.tail = new_node
        new_node.next = new_node
        self.head = new_node
        self.length += 1
        return True

    def pop(self):  # TODO: Review pop
        temp = self.head
        if temp is None:
            return None

        if temp.next is None:
            self.length -= 1
            return temp

        pre = temp
        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None

        self.length -= 1
        return temp

    def pop_first(self):
        temp = self.head
        if temp is None:
            return None
        self.head = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if self.head is None:
            return None
        temp = self.head

        for i in range(index):
            temp = temp.next
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
        return True

    def insert(self, index, value):
        if index > self.length or index < 0:
            return False
        elif index == self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            new_node = Node(value)
            pre = self.get(index - 1)
            temp = self.get(index)
            pre.next = new_node
            new_node.next = temp
            self.length += 1

    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        pre = self.get(index - 1)
        temp = self.get(index)
        pre.next = temp.next
        temp.next = None
        return temp

    def reverse(self):  # TODO: review reverse
        pre = None
        temp = self.head
        while temp.next is not None:
            temp.next

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_list = LinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.print_list()
print("After POP")
print(my_list.pop().value)
print("after pop first")
print(my_list.pop_first().value)
print("Final list")
my_list.print_list()

print()
print(my_list.get(0).value)

print(my_list.get(1).value)
