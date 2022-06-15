import runner_utils as runner
#import pylab as pl
import argparse
import json

def pre_analyze(N, Q, T):
    magnet = simulation(N, Q, T, 1)[0]
    abs_magnet = [abs(m) for m in magnet]
    pl.subplot(2,1,1)
    pl.plot(magnet)
    pl.subplot(2,1,2)
    pl.plot(abs_magnet)
    pl.show()
    #print(abs_magnet)
    print(sum(magnet), sum(abs_magnet), sum(magnet)/len(magnet), sum(abs_magnet)/len(abs_magnet))

def run_simulation(system_size, sweeps_to_equilibrium, temperatures, simulations_to_average_over, sweeps_to_include_in_calculation_fraction):
    magnets = []
    for temp in temperatures:
        magnet = runner.mean_over_simulations(system_size, sweeps_to_equilibrium, temp, simulations_to_average_over, sweeps_to_include_in_calculation_fraction)
        magnets.append(magnet)
        print(temp, magnet)
    return magnets

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

    magnetization_per_temp = run_simulation(system_size,
                                            sweeps_to_equilibrium,
                                            temperatures,
                                            simulations_to_average_over,
                                            sweeps_to_include_in_calculation_fraction)
    # print(magnetization_per_temp)
    # pl.plot(temperatures, magnetization_per_temp)
    # pl.show()

if __name__ == "__main__":
    main()
