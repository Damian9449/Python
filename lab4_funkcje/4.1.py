#!/usr/bin/python

X = "qwerty"

def func():
    global X
    X = "abc"

func()
print (X)