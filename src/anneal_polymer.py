import data_utils
import polymerstatistics as polstat
import system_translation as systrans
import equilibrium as equil
import hamiltonian as ha
import simulation_tools as sim
import argparse
import json
import csv
import statistics as stats
import numba

def anneal_polymer_positions(polymer_positions, connections, sweeps, temperature):
    numba_positions = numba.typed.List(polymer_positions)
    spins = systrans.translate_positions_to_spins(numba_positions)
    equilibrium_spins = equil.equilibrium(spins,
                                          connections,
                                          sweeps,
                                          temperature)
    return systrans.translate_spins_to_positions(equilibrium_spins)

def main():
    parser = argparse.ArgumentParser(description='Anneal Random walk')
    parser.add_argument('polymer_positions_in', metavar='polymer_positions_in', type=str, help='Random walk file in')
    parser.add_argument('connection_file', metavar='connection_file', type=str, help='Connection File')
    parser.add_argument('output_file_polymers', metavar='output_file_polymers', type=str, help='Output Random Walk File ')
    parser.add_argument('sweeps_to_equilibrium', metavar='sweeps_to_equilibrium', type=int, help='Number of sweeps to reach equilibrium')
    parser.add_argument('number_runs', metavar='number_runs', type=int, help='Number of runs')
    parser.add_argument('temperature', metavar='temperature', type=float, help='Temperature')
    args = parser.parse_args()
    f_polyms = open(args.polymer_positions_in)
    reader = csv.reader(f_polyms)
    polymer_positions_strings = list(reader)
    f_polyms.close()
    f_connections = open(args.connection_file)
    connections = json.load(f_connections)
    f_connections.close()

    polymer_positions_start = data_utils.convert_list_list_char_to_int(polymer_positions_strings)
    start_clashes = polstat.count_clashes(polymer_positions_start)
    end_clashes = []
    for i in range(args.number_runs):
        polymer_positions_end =  anneal_polymer_positions(polymer_positions_start,
                                                          connections["connections"],
                                                          args.sweeps_to_equilibrium,
                                                          args.temperature)
        end_clashes.append(polstat.count_clashes(polymer_positions_end))

    print("start:", start_clashes, "end mean:", stats.mean(end_clashes))

if __name__ == "__main__":
    main()
