#!/usr/bin/python

class Node:
    """Klasa reprezentujaca wezel drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def bst_max(top):
    if top is None:
        raise ValueError("Tree is empty")
    maximum = top.data
    if top.left:
        maximum = max(bst_max(top.left), maximum)
    if top.right:
        maximum = max(bst_max(top.right), maximum)
    return maximum


def bst_min(top):
    if top is None:
        raise ValueError("Tree is empty")
    minimum = top.data
    if top.left:
        minimum = min(bst_min(top.left), minimum)
    if top.right:
        minimum = min(bst_min(top.right), minimum)
    return minimum


# root = None           # puste drzewo
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(-5)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(bst_max(root))
print(bst_min(root))
