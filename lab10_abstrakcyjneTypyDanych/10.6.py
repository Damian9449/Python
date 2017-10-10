#!/usr/bin/python

class Node:

    def __init__(self, data=None, priority=0, next=None):
        self.data = data
        self.next = next
        self.priority = priority

    def __str__(self):
        return str(self.data)

class PriorityQueue:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return not self.head

    def insert(self, data):
        node = Node(data)
        # Najwiekszy element chcemy miec na poczatku listy.
        # Robimy widelki do wstawienia nowego elementu.
        before = None
        after = self.head   # moze byc None
        while after:
            if after.data < node.data: break
            before = after
            after = after.next
        if before is None: # przed poczatkiem listy
            node.next = self.head
            self.head = node
        else:  # jestesmy w glebi listy, moze na koncu
            node.next = before.next
            before.next = node

    def remove(self):   # constant-time, bo usuwamy poczatek
        data = self.head.data
        self.head = self.head.next
        return data

    def increase(self, value):
        tmp = self.head
        while tmp:
            tmp.priority += value
            tmp = tmp.next


p = PriorityQueue()
p.insert(1)
p.insert(2)
print("First: ", p.head.priority)
print("Second: ", p.head.next.priority)
print("Increase priority")
p.increase(2)
print("First: ", p.head.priority)
print("Second: ", p.head.next.priority)
print("Increase priority and add element")
p.insert(3)
p.increase(4)
print("First: ", p.head.priority)
print("Second: ", p.head.next.priority)
print("Third: ", p.head.next.next.priority)
