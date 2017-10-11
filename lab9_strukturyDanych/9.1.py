#!/usr/bin/python

class Node:
    """Klasa reprezentujaca wezel listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogolnie


def traverse(node, visit):
    """Iteracyjne przejscie przez liste jednokierunkowa."""
    while node:
        visit(node)
        node = node.next


def visit(node):
    print("node: ", node.data)


def remove_head(node):
    if node is None:
        raise ValueError("List is empty")
    else:
        tmp_ptr, tmp_value = node, node.data
        node = node.next
        del tmp_ptr
        return (node, tmp_value)


def remove_tail(node):
    if node is None:
        raise ValueError("List is empty")
    else:
        head = node
        before = node
        if node.next != None:
            node = node.next
            while node.next != None:
                before = node
                node = node.next

            tmp_value, before.next = node.data, None
            return head, tmp_value
        else:
            return remove_head(head)


head = None                   # [], pusta lista
head = Node(7, head)          # [3]
head = Node(6, head)          # [2, 3]
head = Node(5, head)          # [4, 2, 3]
head = Node(4, head)
head = Node(3, head)
head = Node(2, head)
head = Node(1, head)

print("Before remove head: ")
traverse(head, visit)
head, data = remove_head(head)
print("Element, which was deleted: ", data)
print("After remove head and before remove tail: ")
traverse(head, visit)
head, data = remove_tail(head)
print("After remove tail")
traverse(head, visit)
