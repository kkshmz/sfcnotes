set logscale
set xlabel "counts"
set ylabel "CCDF"

plot	"ccdf.txt" using 1:3 notitle with points
