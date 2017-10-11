#!/usr/bin/python

from collections import deque
from random import randint
from math import floor


class RandomQueue:

    def __init__(self, max_size):
        self.data = deque()
        self.size = 0
        self.maxSize = max_size

    def insert(self, item):
        self.data.append(item)
        self.size += 1

    def remove(self):   # zwraca losowy element
        self.data.rotate(randint(-floor(self.maxSize/2), floor(self.maxSize/2)))
        self.size -= 1
        return self.data.pop()

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.maxSize


k = RandomQueue(5)
k.insert(1)
k.insert(2)
k.insert(3)
k.insert(4)
print(k.remove())
