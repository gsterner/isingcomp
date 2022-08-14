isingsim:
	python3 src/isingsim.py data/test_ising_sim.json

system-setup-test:
	python3 src/system_setup.py 16 system_16.json

equilibrium-test:
	python3 src/equilibrium.py data/system_16.json 100 0.16

polymersim:
	python3 src/polymersim.py polymer.csv

plot-polymersim: polymersim
	gnuplot -e "filename='polymer.csv'" -p src/plotrandomwalk.gnuplot
