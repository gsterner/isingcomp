isingsim:
	python3 src/isingsim.py data/test_ising_sim.json

system-setup-test:
	python3 src/system_setup.py 16 system_16.json

equilibrium-test:
	python3 src/equilibrium.py data/spins_16.json data/connections_16.json 100 0.16

polymersim:
	python3 src/polymersim.py polymer.csv 30

plot-polymersim: polymersim
	gnuplot -e "filename='polymer.csv'; p_range=20" -p src/plotrandomwalk.gnuplot

clash-check:
	python3 src/polymerstatistics.py

plot-clash-check: clash-check
	gnuplot -e "filename='clash_check.csv'; p_range=4" -p src/plotrandomwalk.gnuplot

plot-translated:
	gnuplot -e "filename='translated.csv'; p_range=4" -p src/plotrandomwalk.gnuplot

translate-spin-file-to-random-walk:
	python3 src/system_translation.py $(SPIN_FILE) translated.csv

translate-and-plot-spin-file: translate-spin-file-to-random-walk plot-translated

equilibriate:
	python3 src/equilibrium.py $(SPINS) $(CONNECTIONS) 100 0.16
