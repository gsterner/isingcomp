import walktree
import polymersim as poly
import polymerstatistics as polstat
import system_translation as systrans
import argparse
import numba
import numpy as np

def main():
    parser = argparse.ArgumentParser(description='Simulate many self avoiding random walks')
    parser.add_argument('walk_length',
                        metavar='walk_length',
                        type=int,
                        help='Number of Steps')
    parser.add_argument('number_test_walks',
                        metavar='number_test_walks',
                        type=int,
                        help='Number walks used in simulation')

    #parser.add_argument('output_file', metavar='output_file', type=str, help='Output File')
    args = parser.parse_args()
    unique_walks = walktree.WalkTree()
    number_unique = 0
    root_mean_squares = []
    for i in range(args.number_test_walks):
        polymer_positions = poly.self_avoiding_random_walk_complete(args.walk_length)
        polymer_directions = systrans.positions_to_directions(numba.typed.List(polymer_positions))
        if not unique_walks.has_walk(polymer_directions):
            unique_walks.add_walk(polymer_directions)
            number_unique += 1
            root_mean_squares.append(polstat.root_mean_square(polymer_positions))

        print("run ", i, "number unique:", number_unique, "mean rms:", np.mean(root_mean_squares))

if __name__ == "__main__":
    main()
