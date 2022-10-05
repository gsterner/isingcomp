import data_utils
import polymersim as poly
import system_translation as systrans
import connection_matrix_creation as cmc
import polymerstatistics as polstat
import numpy as np
from numpy import linalg
import argparse
import time

def is_unallowed(polymer_positions):
    return polstat.has_duplicates(polymer_positions)

def is_covered(polymer_positions, unallowed_walks):
    return polymer_positions.__str__() in unallowed_walks

def single_connection_matrix_from_random_walk(polymer_positions):
    spin_system = systrans.translate_positions_to_spins(polymer_positions)
    return cmc.outer_square(spin_system)

def train_connection_matrix(spin_dim, walk_length, no_test_walks):
    percent_step = no_test_walks / 100
    percent_count = 1
    connections_total = np.zeros((spin_dim, spin_dim))
    unallowed_walks = set()
    for i in range(no_test_walks):
        polymer_positions = poly.random_walk(walk_length)
        if is_unallowed(polymer_positions) and not is_covered(polymer_positions, unallowed_walks):
            unallowed_walks.add(polymer_positions.__str__())
            connections_total += single_connection_matrix_from_random_walk(polymer_positions)
        if i > (percent_step * percent_count):
            print(percent_count, "%")
            percent_count += 1
    return unallowed_walks, (-1 * connections_total)

def connection_matrix_simulation(walk_length, no_test_walks):
    spin_dim = 2 * walk_length
    return train_connection_matrix(spin_dim, walk_length, no_test_walks)

def normalize_connection_matrix(connections, no_unallowed_walks):
    return connections / no_unallowed_walks

def main():
    parser = argparse.ArgumentParser(description='Simulate connection matrix')
    parser.add_argument('walk_length',
                        metavar='walk_length',
                        type=int,
                        help='Number of Steps')
    parser.add_argument('number_test_walks',
                        metavar='number_test_walks',
                        type=int,
                        help='Number walks used in simulation')
    parser.add_argument('output_file', metavar='output_file', type=str, help='Output File')
    args = parser.parse_args()
    tic = time.time()
    unallowed_walks, connections_total = connection_matrix_simulation(args.walk_length, args.number_test_walks)
    toc = time.time()
    data_utils.save_connections(connections_total.tolist(), args.output_file)
    connections_normal = normalize_connection_matrix(connections_total, len(unallowed_walks))
    data_utils.save_connections(connections_normal.tolist(), "norm_" + args.output_file)

    print("Number of unalllowed walks",len(unallowed_walks))
    print("Matrix Norm", linalg.norm(connections_total))
    print("Time: ", toc - tic)

if __name__ == "__main__":
    main()
