set boxwidth 0.1
set xlabel "x"
set ylabel "f(x)"
plot "box-muller-hist.txt" using 1:($2/1000) with boxes notitle, \
     1/sqrt(2*pi)*exp(-x**2/2) notitle with lines