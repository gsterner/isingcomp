import polymersim as polsim
from polymersim import Direction
import argparse
import json

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

def translate_system(spin_system):
    splitted_spin_system = split_spins_into_pairs(spin_system)
    directions = [translate_spin_pair_to_direction(spin_pair) for spin_pair in splitted_spin_system]
    return random_walk_from_directions(directions)

def main():
    parser = argparse.ArgumentParser(description='Translate spin system to random walk')
    parser.add_argument('input_file', metavar='input_file', type=str, help='Input File')
    parser.add_argument('output_file', metavar='output_file', type=str, help='Output File')
    args = parser.parse_args()
    f = open(args.input_file)
    input_data = json.load(f)
    f.close()

    spin_system = input_data["spins"]
    polymer_positions = translate_system(spin_system)
    polsim.dump_random_walk_to_csv(args.output_file, polymer_positions)

if __name__ == "__main__":
    main()
