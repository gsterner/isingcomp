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

translate-spin-output-to-random-walk:
	python3 src/system_translation.py spins_output.json translated.csv

translate-spin-output-to-walk-and-plot: translate-spin-output-to-random-walk plot-translated

translate-original-spin-to-random-walk:
	python3 src/system_translation.py data/spins_4.json translated.csv

translate-original-spin-to-walk-and-plot: translate-original-spin-to-random-walk plot-translated

equilibriate-four-spins:
	python3 src/equilibrium.py data/spins_4.json data/connections_4.json 100 0.16
