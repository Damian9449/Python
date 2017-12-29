set term png
set output "sort11.png"

set title "Sortowanie X"
set xlabel "numer pozycji"              # opis osi x
set ylabel "liczba na pozycji"          # opis osi y
unset key                               # bez legendy

plot "sort11.dat" using 1:2 with points pt 5