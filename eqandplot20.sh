gnuplot -e "filename='data/test20/start.csv'; p_range=12; set title 'START'; show title" -p src/plotrandomwalk.gnuplot
python3 src/system_translation.py --translation positions_to_spins data/test20/start.csv data/test20/start_spins.json
python3 src/equilibrium.py data/test20/start_spins.json data/test20/norm_sim_conn_20.json data/test20/spins_output.json 20 0.01
python3 src/system_translation.py data/test20/spins_output.json data/test20/end.csv
gnuplot -e "filename='data/test20/end.csv'; p_range=12; set title 'END'; show title" -p src/plotrandomwalk.gnuplot
