import data_utils
import polymerstatistics as polstat
import system_translation as systrans
import equilibrium as equil
import hamiltonian as ha
import simulation_tools as sim
import argparse
import json
import csv

def main():
    parser = argparse.ArgumentParser(description='Anneal Random walk')
    parser.add_argument('polymer_positions_in', metavar='polymer_positions_in', type=str, help='Random walk file in')
    parser.add_argument('connection_file', metavar='connection_file', type=str, help='Connection File')
    parser.add_argument('output_file_polymers', metavar='output_file_polymers', type=str, help='Output Random Walk File ')
    parser.add_argument('sweeps_to_equilibrium', metavar='sweeps_to_equilibrium', type=int, help='Number of sweeps to reach equilibrium')
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
    spins = systrans.translate_positions_to_spins(polymer_positions_start)

    equilibrium_spins = equil.equilibrium(spins,
                                          connections["connections"],
                                          args.sweeps_to_equilibrium,
                                          args.temperature)

    polymer_positions_end = systrans.translate_spins_to_positions(equilibrium_spins)

    start_energy = ha.hamiltonian_of_system(spins, connections["connections"])
    end_energy = ha.hamiltonian_of_system(equilibrium_spins, connections["connections"])
    print("Start Energy: ", start_energy, "End Energy :", end_energy)
    print("Start Clashes: ", polstat.count_clashes(polymer_positions_start), "End clashes", polstat.count_clashes(polymer_positions_end))
    print("Temperature: ", args.temperature, "Magnetization: ", sim.magnetization(equilibrium_spins))

if __name__ == "__main__":
    main()
