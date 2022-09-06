isingsim:
	python3 src/isingsim.py data/test_ising_sim.json

system-setup-test:
	python3 src/system_setup.py 16 system_16.json

equilibrium-test:
	python3 src/equilibrium.py data/spins_16.json data/connections_16.json 100 0.16

polymersim:
	python3 src/polymersim.py polymer.csv $(LENGTH)

plot-polymersim: polymersim
	gnuplot -e "filename='polymer.csv'; p_range=20" -p src/plotrandomwalk.gnuplot

clash-check:
	python3 src/polymerstatistics.py

plot-clash-check: clash-check
	gnuplot -e "filename='clash_check.csv'; p_range=4" -p src/plotrandomwalk.gnuplot

plot-translated:
	gnuplot -e "filename='translated.csv'; p_range=4" -p src/plotrandomwalk.gnuplot

plot-polymer:
	gnuplot -e "filename='$(POLYMER)'; p_range=4; set title '$(POLYMER)'; show title" -p src/plotrandomwalk.gnuplot

translate-spin-file-to-random-walk:
	python3 src/system_translation.py $(SPIN_FILE) translated.csv

translate-polymer-to-spin-file:
	python3 src/system_translation.py --translation positions_to_spins polymer.csv translated.json

translate-and-plot-spin-file: translate-spin-file-to-random-walk plot-translated

equilibriate:
	python3 src/equilibrium.py $(SPINS) $(CONNECTIONS) 100 0.16

test-translation-from-spins-to-positions:
	python3 src/system_translation.py --translation spins_to_positions data/spins_4.json translated.csv

test-translation-from-positions-to-spins:
	python3 src/system_translation.py --translation positions_to_spins data/positions.csv translated.json

#make equilibriate-poly LENGTH=2 SPINS=translated.json CONNECTIONS=data/connections_4.json SPIN_FILE=spins_output.json POLYMER=polymer.csv
equilibriate-poly: polymersim translate-polymer-to-spin-file equilibriate translate-and-plot-spin-file plot-polymer
