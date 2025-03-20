class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value=value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True

    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None

        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value):
        new_node = Node(value=value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

        return True

    def pop_first(self) -> Node:
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index) -> Node:
        if index >= self.length or index < 0:
            return None

        result = self.head
        for _ in range(index):
            result = result.next

        return result

    def set_value(self, index, value) -> bool:
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index > self.length or index < 0:
            return False
        elif index == self.length:
            return self.append(value=value)
        elif index == 0:
            return self.prepend(value=value)

        temp = self.get(index)
        pre = self.get(index=index - 1)
        new_node = Node(value=value)
        new_node.next = temp
        pre.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()

        temp = self.get(index=index)
        pre = self.get(index=index - 1)
        pre.next = temp.next
        temp.next = None

        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(4)
my_linked_list.append(9)
my_linked_list.append(3)
my_linked_list.prepend(8)
my_linked_list.print_list()

print()
my_linked_list.set_value(index=2, value=2)
my_linked_list.print_list()


print()
my_linked_list.insert(index=3, value=5)
my_linked_list.print_list()

print()
my_linked_list.insert(index=4, value=2)
my_linked_list.print_list()

print()
my_linked_list.insert(index=0, value=2)
my_linked_list.print_list()


print()
my_linked_list.remove(index=2)
my_linked_list.print_list()

print()
my_linked_list.reverse()
my_linked_list.print_list()
