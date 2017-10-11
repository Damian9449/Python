#!/usr/bin/python


class Node:
    """Class representing node"""
    def __init__(self, data=1, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.data)


class BinaryTree:
    """Class representing binary tree"""

    # private
    __head = None
    __counter = 0

    def depth_rek(self, leaf):
        if leaf is not None:
            return 1 + max(self.depth_rek(leaf.left), self.depth_rek(leaf.right))
        else:
            return 0

    # poprawic rekurencje
    def __search_rec(self, element, leaf):
        if leaf.data is element:
            return True
        else:
            if element < leaf.data:
                if leaf.left is not None:
                    self.__search_rec(element, leaf.left)
                else:
                    return False
            else:
                if leaf.right is not None:
                    self.__search_rec(element, leaf.right)
                else:
                    return False

    def __print_inorder_rek(self, leaf):
        if leaf is not None:
            self.__print_inorder_rek(leaf.left)
            print(leaf.data)
            self.__print_inorder_rek(leaf.right)

    def __print_postorder_rek(self, leaf):
        if leaf is not None:
            self.__print_postorder_rek(leaf.left)
            self.__print_postorder_rek(leaf.right)
            print(leaf.data)

    def __print_preorder_rek(self, leaf):
        if leaf is not None:
            print(leaf.data)
            self.__print_preorder_rek(leaf.left)
            self.__print_preorder_rek(leaf.right)

    def __next_leaf(self, element, node):
        if element < node.data:
            if node.left is not None:
                self.__next_leaf(element, node.left)
            else:
                node.left = Node(element)
                node.left.parent = node
                self.__counter = self.__counter + 1
        else:
            if node.right is not None:
                self.__next_leaf(element, node.right)
            else:
                node.right = Node(element)
                node.right.parent = node
                self.__counter = self.__counter + 1

    # public
    def __init__(self):
        self.__head = Node()

    def __del__(self):
       # print("Usuwamy")
        pass

    def insert(self, element):
        if self.__counter is 0:
            self.__head.data = element
            self.__counter = self.__counter + 1
        else:
            self.__next_leaf(element, self.__head)

    def depth(self):
        return self.depth_rek(self.__head)

    def size(self):
        return self.__counter

    def maximum(self):
        tmp = self.__head

        while tmp.right is not None:
            tmp = tmp.right

        return tmp.data

    def minimum(self):
        tmp = self.__head

        while tmp.left is not None:
            tmp = tmp.left

        return tmp.data

    def search(self, element):
        return self.__search_rec(element, self.__head)

    def print_inorder(self):
        self.__print_inorder_rek(self.__head)

    def print_postorder(self):
        self.__print_postorder_rek(self.__head)

    def print_preorder(self):
        self.__print_preorder_rek(self.__head)


