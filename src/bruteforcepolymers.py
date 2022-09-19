import argparse
import data_utils
import polymersim as polsim

def main():
    parser = argparse.ArgumentParser(description='Generate ALL polymer with given length')
    parser.add_argument('number_steps',
                        metavar='number_steps',
                        type=int,
                        help='Number of Steps')
    parser.add_argument('output_file', metavar='output_file', type=str, help='Output File')
    args = parser.parse_args()
    position_configs = polsim.brute_force_position_configs(args.number_steps)
    out_data_columnwise = data_utils.order_positions_columnwise(position_configs)
    data_utils.dump_random_walk_to_csv(args.output_file, out_data_columnwise)

if __name__ == "__main__":
    main()
