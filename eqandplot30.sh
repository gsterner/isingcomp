gnuplot -e "filename='data/test30/start.csv'; p_range=12; set title 'START'; show title" -p src/plotrandomwalk.gnuplot
python3 src/system_translation.py --translation positions_to_spins data/test30/start.csv data/test30/start_spins.json
python3 src/equilibrium.py data/test30/start_spins.json data/test30/sim_conn_30_1000000.json data/test30/spins_output.json 20 0.01
python3 src/system_translation.py data/test30/spins_output.json data/test30/end.csv
gnuplot -e "filename='data/test30/end.csv'; p_range=12; set title 'END'; show title" -p src/plotrandomwalk.gnuplot
