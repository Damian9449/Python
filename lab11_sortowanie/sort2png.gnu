set term png
set output "sort2.png"

set title "Sortowanie X"
set xlabel "numer pozycji"              # opis osi x
set ylabel "liczba na pozycji"          # opis osi y
unset key                               # bez legendy

plot "sort2.dat" using 1:2 with points pt 5