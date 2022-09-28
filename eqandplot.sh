python3 src/system_translation.py translated.json data/test10/start.csv
gnuplot -e "filename='start.csv'; p_range=12; set title 'START'; show title" -p src/plotrandomwalk.gnuplot
#python3 src/equilibrium.py translated.json data/test10/connections_all.json 1 0
#I am interested in generating many different walks, so in this case few sweeps is good
#The interesting question is why I get as good results with matrix with only ones
#python3 src/equilibrium.py translated.json data/test10/equal_connections.json 1 0
python3 src/equilibrium.py translated.json data/test10/banded_connections.json 1 0
python3 src/system_translation.py spins_output.json end.csv
gnuplot -e "filename='end.csv'; p_range=12; set title 'END'; show title" -p src/plotrandomwalk.gnuplot
