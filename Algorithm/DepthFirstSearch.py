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


def DFSPreOrder(tree):

    temp = []

    def traverse(node):
        temp.append(node.value)
        if node.left is not None:
            traverse(node.left)
        if node.right is not None:
            traverse(node.right)

    traverse(tree.root)
    return temp


if __name__ == "__main__":

    my_tree = bst.BinarySearchTree()
    my_tree.insert(9)
    my_tree.insert(10)
    my_tree.insert(11)
    my_tree.insert(5)
    my_tree.insert(3)
    my_tree.insert(15)
    my_tree.insert(16)

    print(DFSPreOrder(my_tree))

#             9
#         5         10
#    3                   11
#                               15
#                                        16
