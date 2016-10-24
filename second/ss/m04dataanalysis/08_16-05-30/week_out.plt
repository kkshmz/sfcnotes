set xlabel "time (2 hour interval)"
set xtic 2
set xrange [-1:23]
set yrange [0:]
set key top left
set ylabel "Traffic (Mbps)"

plot	"week_out.txt" using 1:($2/1000000) title 'Mon' with lines, \
	"week_out.txt" using 1:($3/1000000) title 'Tue' with lines, \
	"week_out.txt" using 1:($4/1000000) title 'Wed' with lines, \
	"week_out.txt" using 1:($5/1000000) title 'Thu' with lines, \
	"week_out.txt" using 1:($6/1000000) title 'Fri' with lines, \
	"week_out.txt" using 1:($7/1000000) title 'Sat' with lines, \
	"week_out.txt" using 1:($8/1000000) title 'Sun' with lines
