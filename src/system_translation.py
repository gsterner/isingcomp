import polymersim as polsim
from polymersim import Direction
import argparse
import json
import csv

def convert_list_list_char_to_int(outer_list):
    return [[int(char_element) for char_element in inner_list] for inner_list in outer_list]

def translate_spin_pair_to_direction(spin_pair):
    if spin_pair == (1,1):
        return Direction.NORTH
    if spin_pair == (1,-1):
        return Direction.EAST
    if spin_pair == (-1, 1):
        return Direction.WEST
    return Direction.SOUTH

def split_spins_into_pairs(spin_system):
    return [tuple(spin_system[i:i+2]) for i in range(0, len(spin_system), 2)]

def random_walk_from_directions(directions):
    START = [0,0]
    positions = [START]
    for direction in directions:
        step = polsim.step_from_direction(direction)
        positions = polsim.update_position(positions, step)
    return positions

def translate_spins_to_positions(spin_system):
    splitted_spin_system = split_spins_into_pairs(spin_system)
    directions = [translate_spin_pair_to_direction(spin_pair) for spin_pair in splitted_spin_system]
    return random_walk_from_directions(directions)

def translate_positions_to_spins(positions):
    print(positions)

def main():
    parser = argparse.ArgumentParser(description='Translate spin system to random walk')
    parser.add_argument('--translation',
                        default='spins_to_positions',
                        const='spins_to_positions',
                        nargs='?',
                        choices=['positions_to_spins', 'spins_to_positions'],
                        help='Choose translation direction (default: %(default)s)')
    parser.add_argument('input_file', metavar='input_file', type=str, help='Input File')
    parser.add_argument('output_file', metavar='output_file', type=str, help='Output File')
    args = parser.parse_args()

    if args.translation == 'spins_to_positions':
        f = open(args.input_file)
        input_data = json.load(f)
        f.close()
        spin_system = input_data["spins"]
        polymer_positions = translate_spins_to_positions(spin_system)
        polsim.dump_random_walk_to_csv(args.output_file, polymer_positions)
    else:
        f = open(args.input_file)
        reader = csv.reader(f)
        input_data= list(reader)
        f.close()
        positions_in = convert_list_list_char_to_int(input_data)
        translate_positions_to_spins(positions_in)

if __name__ == "__main__":
    main()
