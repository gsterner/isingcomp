import simulation_tools as simtools
import generate_system as gs
import argparse
import json
import math

def is_square(n):
    return math.sqrt(n).is_integer()

def generate_system(system_size):
    spins, connections = simtools.setup_nearest_neigbour_system(system_size, int(math.sqrt(system_size)))
    return {"spins":spins, "connections":connections}

def save_output(system_data, file_name):
    with open(file_name, 'w') as f:
        json.dump(system_data, f)
        f.close()

def main():
    parser = argparse.ArgumentParser(description='Generate spin system file')
    parser.add_argument('system_size', metavar='system_size', type=int, help='System Size')
    parser.add_argument('output_file', metavar='output_file', type=str, help='Output File')

    #parser.add_argument('system_type', metavar='system_type', type=str, help='System Type')
    args = parser.parse_args()
    if not is_square(args.system_size):
        raise Exception("Only symmetric systems are allowed. System size must be a square")
    spins, connections = simtools.setup_nearest_neigbour_system(args.system_size, int(math.sqrt(args.system_size)))
    system = generate_system(args.system_size)
    save_output(system, args.output_file)

if __name__ == "__main__":
    main()
