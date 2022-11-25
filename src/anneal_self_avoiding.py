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
import numpy as np

def anneal_polymer_positions(polymer_positions, connections, sweeps, temperature):
    numba_positions = numba.typed.List()
    for pos in polymer_positions:
        numba_positions.append(numba.typed.List(pos))
    spins = systrans.translate_positions_to_spins(numba_positions)
    equilibrium_spins = equil.equilibrium(spins,
                                          connections,
                                          sweeps,
                                          temperature)
    return systrans.translate_spins_to_positions(numba.typed.List(equilibrium_spins))

def anneal_polymer_positions_profile(polymer_positions, connections, sweeps_profile, temperature_profile):
    numba_positions = numba.typed.List()
    for pos in polymer_positions:
        numba_positions.append(numba.typed.List(pos))
    spins = systrans.translate_positions_to_spins(numba_positions)
    for p_index in range(len(sweeps_profile)):
        spins = equil.equilibrium(spins,
                                  connections,
                                  sweeps_profile[p_index],
                                  temperature_profile[p_index])
    return systrans.translate_spins_to_positions(numba.typed.List(spins))

def convert_histogram_edges_to_mids(edges):
    distance = edges[1:] - edges[:-1]
    mids = edges[:-1] + distance / 2
    return mids

def main():
    parser = argparse.ArgumentParser(description='Anneal Random walk')
    parser.add_argument('polymer_positions_in', metavar='polymer_positions_in', type=str, help='Random walk file in')
    parser.add_argument('connection_file', metavar='connection_file', type=str, help='Connection File')
    parser.add_argument('output_file', metavar='output_file', type=str, help='Output File ')
    parser.add_argument('temperature_profile', metavar='temperature_profile', type=str, help='Temperature and sweeps profile file in')
    parser.add_argument('number_runs', metavar='number_runs', type=int, help='Number of runs')

    args = parser.parse_args()
    f_polyms = open(args.polymer_positions_in)
    reader = csv.reader(f_polyms)
    polymer_positions_strings = list(reader)
    f_polyms.close()
    f_connections = open(args.connection_file)
    connections = json.load(f_connections)
    f_connections.close()
    f_temp_profile = open(args.temperature_profile)
    temperature_profile = json.load(f_temp_profile)
    f_temp_profile.close()

    polymer_positions_start = data_utils.convert_list_list_char_to_int(polymer_positions_strings)
    start_clashes = polstat.count_clashes(polymer_positions_start)
    for i in range(args.number_runs):
        polymer_positions_end =  anneal_polymer_positions_profile(polymer_positions_start,
                                                                  connections["connections"],
                                                                  temperature_profile["sweeps"],
                                                                  temperature_profile["temperature"])
    end_clashes = polstat.count_clashes(polymer_positions_end)
    print("start:", start_clashes, "end mean:", end_clashes)
    data_utils.dump_random_walk_to_csv(args.output_file, polymer_positions_end)

if __name__ == "__main__":
    main()
