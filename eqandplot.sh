python3 src/system_translation.py translated.json data/test10/start.csv
gnuplot -e "filename='start.csv'; p_range=12; set title 'START'; show title" -p src/plotrandomwalk.gnuplot
python3 src/equilibrium.py translated.json data/test10/connections_all.json 500 0.5
#python3 src/equilibrium.py translated.json data/test10/equal_connections.json 500 0.5
python3 src/system_translation.py spins_output.json end.csv
gnuplot -e "filename='end.csv'; p_range=12; set title 'END'; show title" -p src/plotrandomwalk.gnuplot
