set xlabel "timelag k (minutes)"
set ylabel "auto correlation"
set xrange [-100:5140]
set yrange [0:1]

plot	"autocorr.txt" using ($1*5):2 notitle with lines
