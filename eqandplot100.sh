gnuplot -e "filename='data/test100/start.csv'; p_range=20; set title 'START'; show title" -p src/plotrandomwalk.gnuplot
python3 src/system_translation.py --translation positions_to_spins data/test100/start.csv data/test100/start_spins.json
python3 src/equilibrium.py data/test100/start_spins.json data/test100/sim_conn_100_10000000.json data/test100/spins_output.json 1 0
python3 src/system_translation.py data/test100/spins_output.json data/test100/end.csv
gnuplot -e "filename='data/test100/end.csv'; p_range=20; set title 'END'; show title" -p src/plotrandomwalk.gnuplot
