#!/usr/bin/python
import random

def random_number(n):
	L = []
	L.extend(range(n));
	for i in range(n/2):
		first, second = random.randrange(0, n, 1), random.randrange(0, n, 1)
		L[first], L[second] = L[second], L[first]
		
	return L


def sort_number(n):
	L = []
	L.extend(range(n)); 
	for i in range(n/10):
		first = random.randrange(0, n-1, 1)
		second = first + 1
		L[first], L[second] = L[second], L[first]
	return L


def reverse_number(n):
	L = []
	L.extend(range(n-1,-1,-1))
	for i in range(n/10):
		first = random.randrange(0, n-1, 1)
		second = first + 1
		L[first], L[second] = L[second], L[first]
	return L	
	
	
def gauss_number(n):
	L = []
	for i in range(n):
		L.append(round(random.gauss(1,1), 4))
		
	return L
	
	
def repeated_number(n):
	from math import sqrt
	L = []
	k = int(sqrt(n))
	for i in range(n):
		L.append(random.randrange(0,k))
	
	return L
