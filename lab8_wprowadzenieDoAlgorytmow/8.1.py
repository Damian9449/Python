###############################################################

# SPECYFIKACJA
# Problem: Rozwiązywanie równania liniowego a x + b y + c = 0,
#           o danych współczynnikach
#
# DANE WEJŚCIOWE
# Trzy liczby a, b i c, będące wspołczynnikami równania
#
# DANE WYJŚCIOWE
# (x, y) - rozwiazanie rownania

###############################################################

# Lista krokow:
# 1. Wyznacz NWD wspolczynikow a i b
# 2. Sprawdz czy NWD(a i b) | c
# 3. Jesli nie to zakoncz dzialanie algorytmu, w przeciwnym
#    razie wyznacz X0 i Y0 za pomoca rozszerzonego algorytmu
#    Euklidesa
# 4. Rozwiazania rownania to:
#    a) x = x0 + b/d*t
#    b) y = y0 - a/d*t   ,gdzie t nalezy do liczb calkowitych

###############################################################


def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""

    def nwd(m1, m2):
        while m2 != 0:
            m2, m1 = m1 % m2, m2
        return m1

    def euklides(a, b, c):
        x, lastX = 0, c
        y, lastY = c, 0
        while (b != 0):
            q = a // b
            a, b = b, a % b
            x, lastX = lastX - q * x, x
            y, lastY = lastY - q * y, y
        return lastX, lastY


    if c % nwd(a, b) == 0:
        x0, y0 = euklides(a, b, c)
        print("Rozwiazanie: x = ", x0, " + ", b/nwd, "t, gdzie t nalezy do liczb calkowitych \n" 
                  "\t \t \t y = ", y0, " + ", a/nwd, "t, gdzie t nalezy do liczb calkowitych"  )
    else:
        print("Rownanie nie ma rozwiazania")


solve1(3, 5, 11)
