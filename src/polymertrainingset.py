import argparse
import csv
import data_utils
import polymerstatistics as polstat
import polymersim as polsim

def filter_clash_polymers(position_configs_in):
    clash_polymers = []
    for config in position_configs_in:
        if polstat.has_duplicates(config):
            clash_polymers.append(config)
    return clash_polymers

def main():
    parser = argparse.ArgumentParser(description='Generate training set for connection matrix')
    parser.add_argument('input_file', metavar='input_file', type=str, help='Input File')
    parser.add_argument('output_file', metavar='output_file', type=str, help='Output File')
    args = parser.parse_args()
    f = open(args.input_file)
    reader = csv.reader(f)
    input_data= list(reader)
    f.close()
    data_as_matrix = data_utils.position_config_csv_to_matrix(input_data)
    clash_polymers = filter_clash_polymers(data_as_matrix)
    out_data_columnwise = data_utils.order_positions_columnwise(clash_polymers)
    data_utils.dump_random_walk_to_csv(args.output_file, out_data_columnwise)

if __name__ == "__main__":
    main()
