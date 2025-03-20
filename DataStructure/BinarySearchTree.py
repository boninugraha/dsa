class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        temp = self.root

        if self.root is None:
            self.root = new_node
            return True

        while True:
            if value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            elif value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                return False

    def contains(self, value):
        temp = self.root

        while temp is not None:
            if value == temp.value:
                return True

            elif value < temp.value:
                temp = temp.left

            elif value > temp.value:
                temp = temp.right

        return False


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert(10)
    bst.insert(11)
    bst.insert(8)
    bst.insert(1)
    print(bst.root.value)
    print(bst.root.right.value)
    print(bst.root.left.value)
    print(bst.root.right.right.value)
    print(bst.contains(1))
    print(bst.contains(8))
    print(bst.contains(9))
    print(bst.contains(10))
    print(bst.contains(11))
    print(bst.contains(12))
