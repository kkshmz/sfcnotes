set xlabel "time (2 hour interval)"
set xtic 2
set xrange [-1:23]
set yrange [0:]
set key top left
set ylabel "Traffic (Mbps)"

plot	"hourly_out.txt" using 1:($3/1000000) title 'mean' with lines, \
	"hourly_out.txt" using 1:($3/1000000):($4/1000000) title "stddev" with yerrorbars
