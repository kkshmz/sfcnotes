set logscale x
set xrange [2:4192]
set key bottom
set xtics (4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048)
set grid ytics
set xlabel "sample size"
set ylabel "measurements"

plot	"conf-interval.txt" title "mean" with lines, \
	"conf-interval.txt" using 1:2:4 title "95% confidence interval" with yerrorbars
