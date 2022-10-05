gnuplot -e "filename='polymer.csv'; p_range=20; set title 'START'; show title" -p src/plotrandomwalk.gnuplot
python3 src/system_translation.py --translation positions_to_spins polymer.csv start_spins.json
python3 src/equilibrium.py start_spins.json norm_sim_conn_100.json 100 0.2
python3 src/system_translation.py spins_output.json end.csv
gnuplot -e "filename='end.csv'; p_range=20; set title 'END'; show title" -p src/plotrandomwalk.gnuplot
