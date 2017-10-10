#!/usr/bin/python

class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementow na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full() == False:
            self.items[self.n] = data
            self.n = self.n + 1
        else:
            raise Exception("Stack is full !!!")

    def pop(self):
        if self.is_empty() == False:
            self.n = self.n - 1
            data = self.items[self.n]
            self.items[self.n] = None    # usuwam referencje
            return data
        else:
            raise Exception("Stack is empty !!!")


import unittest


class TestStack(unittest.TestCase):

    def setUp(self):
        self.st1 = Stack(1)
        self.st2 = Stack(0)
        self.st3 = Stack(2)

    def test_pop(self):
        self.assertRaises(Exception, self.st1.pop)

    def test_remove(self):
        self.assertRaises(Exception, self.st2.push)

    def test_isFull(self):
        self.st3.push(1)
        self.st3.push(2)
        self.assertTrue(self.st3.is_full())

    def test_isEmpty(self):
        self.assertTrue(self.st3.is_empty())


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
