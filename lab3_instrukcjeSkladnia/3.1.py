# W pierwszym przykladzie, ktory jest umieszczony ponizej
# niepoprawnym skladniowo sa sredniki na koncu linijek, 
# srednik rozdzielajacy zmienna x i y jest poprawny ale
# trzy pozostale sredniki sa niepotrzebne
# Kolejna niepotrzebna rzecza w tym przykladzie jest 
# nawias umieszczony w warunku petli if

x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;

	
# W drugim przykladzie, ktory jest umieszczony ponizej
# niepoprawne skladniowo jest umieszczenie petli if
# zaraz po for w tej samej linijce

for i in "qwerty": if ord(i) < 150: print(i)


# Trzeci przyklad podany ponizej jest poprawny skladniowo
# w Pythonie, jedyna uwaga jaka sie tutaj nasuwa to rozdzielenie
# popownan w petlach w osobnych linijkach

for i in "axby": print(ord(i) if ord(i) < 100 else i)
