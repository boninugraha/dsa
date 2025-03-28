import sys
import os

# Assuming your package is in a folder named 'my_package'
# and it's located in a directory 'path/to'
package_path = os.path.abspath("DataStructure")

# Add the package path to sys.path
if package_path not in sys.path:
    sys.path.append(package_path)

import BinarySearchTree as bst
import Stacks as st


def BFS(tree, target):
    temp = st.Stacks(tree.root)
    temp2 = st.Stacks(1)
    temp2.hop()

    while temp.top is not None:
        current_value = temp.hop()
        # print(current_value.value.value)
        if current_value.value.left:
            temp2.push(current_value.value.left)
        if current_value.value.right:
            temp2.push(current_value.value.right)
        if current_value.value.value == target:
            return True
        if temp.top is None:
            temp = temp2
    return False


def BFS_Flatten_Tree(tree):
    temp = [tree.root]
    all_node = []

    while temp:
        current_node = temp.pop(0)
        all_node.append(current_node.value)
        if current_node.left is not None:
            temp.append(current_node.left)

        if current_node.right is not None:
            temp.append(current_node.right)

    return all_node


if __name__ == "__main__":

    my_tree = bst.BinarySearchTree()
    my_tree.insert(9)
    my_tree.insert(10)
    my_tree.insert(11)
    my_tree.insert(5)
    my_tree.insert(3)
    my_tree.insert(15)
    my_tree.insert(16)

    # print(BFS(my_tree, 9))
    # print(BFS(my_tree, 6))
    # print(BFS(my_tree, 16))

    print(BFS_Flatten_Tree(my_tree))

#             9
#         5         10
#    3                   11
#                               15
#                                        16
