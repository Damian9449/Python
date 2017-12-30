#!/usr/bin/python
# -*- coding: utf-8 -*-

###############################################################

# SPECYFIKACJA
# Problem: Rozwiazywanie rownania liniowego a x + b y + c = 0,
#           o danych wspolczynnikach
#
# DANE WEJSCIOWE
# Trzy liczby a, b i c, bedace wspolczynnikami rownania
#
# DANE WYJSCIOWE
# (x, y) - rozwiazanie rownania

###############################################################

# Lista krokow:
# A. Sprawdz podane argumenty, jesli sa poprawne wykonaj:
#   1. Sprawdz czy a==0 i b==0 i c!=0, jesli tak, wyswietl komunikat, że "Rownanie sprzeczne - nie ma rozwiazania"
#   2. Sprawdz czy a, b, c sa równe 0, jesli tak, wyswietl komunikat, że "Rownanie nieoznaczone - nieskonczenie wiele rowiazan"
#   3. Sprawdz czy a==0 i b!=0, jesli tak, wyswietl komunikat "Rozwiazanie: y = -c/b"
#   4. Sprawdz czy a!=0 i b==0, jesli tak, wyswietl komunikat "Rozwiazanie: x = -c/a"
#   5. W przeciwnym razie wyswietl komunikat "Rozwiazanie: y= x* -a/b  -c/b,  x nalezy do liczb rzeczywistych"
# B. Jesli nie rzuc wyjątek ValueError("Podales zle argumenty")

###############################################################


def solve1(a, b, c):
    """Rozwiazywanie rownania liniowego a x + b y + c = 0."""
    if (type(a) is (int or float)) and (type(b) is (int or float)) and (type(c) is (int or float)):
        if a == 0 and b == 0 and c != 0:
            print "Rownanie sprzeczne - nie ma rozwiazania"
        elif a == 0 and b == 0 and c == 0:
            print "Rownanie nieoznaczone - nieskonczenie wiele rowiazan"
        elif a == 0 and b != 0:
            print "Rozwiazanie: y = "+str(-c*1.0/b)
        elif a != 0 and b == 0:
            print "Rozwiazanie: x = "+str(-c*1.0/a)
        else:
            print "Rozwiazanie: y = x*"+str(-a*1.0/b) + " + " + str(-c*1.0/b) + ", x nalezy do liczb rzeczywistych"
    else:
        raise ValueError("Podales zle argumenty")

solve1(5, 1, 55)
