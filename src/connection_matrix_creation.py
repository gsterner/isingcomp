import data_utils
import numpy as np
import argparse
import json

def outer_square(spins_np):
    return np.outer(spins_np, spins_np)

def zero_connection_np_matrix(spin_configs):
    spin_size = len(spin_configs[0]["spins"])
    dimension = (spin_size, spin_size)
    return np.zeros(dimension)

def shift_to_cost_minimization(connections):
    return -1 * connections

def estimate_connections(spin_configs):
    connections_sum = zero_connection_np_matrix(spin_configs)
    for spins in spin_configs:
        spins_np = np.array(spins["spins"])
        connections_np = outer_square(spins_np)
        connections_sum += connections_np
    connections_sum = shift_to_cost_minimization(connections_sum)
    connections_sum = connections_sum.astype(int)
    return connections_sum.tolist()

def main():
    parser = argparse.ArgumentParser(description='Create connection matrix that maximises cost for spin config')
    parser.add_argument('spin_file', metavar='spin_file', type=str, help='Spin File')
    args = parser.parse_args()
    f_spins = open(args.spin_file)
    spins = json.load(f_spins)
    f_spins.close()
    connections = estimate_connections(spins["spin_configs"])
    data_utils.save_connections(connections, "connections_output.json")

if __name__ == "__main__":
    main()
