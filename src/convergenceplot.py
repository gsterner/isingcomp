import equilibrium as equilib
import pylab as pl
import argparse
import json

def run_simulation(system_size, sweeps_to_equilibrium, temperatures):
    temp = temperatures[0]
    return equilib.equilibriate(system_size, sweeps_to_equilibrium, temp)

def main():
    parser = argparse.ArgumentParser(description='Run ising simulation from input file')
    parser.add_argument('input_file', metavar='input_file', type=str, help='Input File')
    args = parser.parse_args()
    f = open(args.input_file)
    input_data = json.load(f)
    f.close()

    temperatures = input_data['temperatures']
    system_size = input_data['system_size']
    sweeps_to_equilibrium = input_data['sweeps_to_equilibrium']
    simulations_to_average_over = input_data['simulations_to_average_over']
    sweeps_to_include_in_calculation_fraction = input_data['sweeps_to_include_in_calculation_fraction']

    magnetization_per_sweep = run_simulation(system_size,
                                            sweeps_to_equilibrium,
                                            temperatures)

    sweep = range(sweeps_to_equilibrium)
    pl.plot(sweep, magnetization_per_sweep)
    pl.show()

if __name__ == "__main__":
    main()
