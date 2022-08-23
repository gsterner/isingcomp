set datafile separator ','
set xrange [-p_range:p_range]
set yrange [-p_range:p_range]
plot filename using 1:2 with lines
