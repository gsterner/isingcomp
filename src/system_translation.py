import polymersim as polsim
from polymersim import Direction
import simulation_tools
import data_utils
import argparse
import json
import csv
import numba
from numba import jit

@jit(nopython=True)
def spin_pair_to_direction(spin_pair):
    if spin_pair == (1,1):
        return Direction.NORTH
    if spin_pair == (1,-1):
        return Direction.EAST
    if spin_pair == (-1, 1):
        return Direction.WEST
    return Direction.SOUTH

@jit(nopython=True)
def direction_to_spin_pair(direction):
    if direction == Direction.NORTH:
        return (1,1)
    if direction == Direction.EAST:
        return (1,-1)
    if direction == Direction.WEST:
        return (-1,1)
    return (-1,-1)

@jit(nopython=True)
def position_pair_to_direction(prev_position, next_position):
    direction_as_array = (next_position[0] - prev_position[0], next_position[1] - prev_position[1])
    if direction_as_array == (0,1):
        return Direction.NORTH
    if direction_as_array == (1,0):
        return Direction.EAST
    if direction_as_array == (-1, 0):
        return Direction.WEST
    return Direction.SOUTH

@jit(nopython=True)
def split_spins_into_pairs(spin_system):
    return [(spin_system[i], spin_system[i+1]) for i in range(0, len(spin_system), 2)]

@jit(nopython=True)
def positions_to_directions(positions):
    directions = []
    for i in range(len(positions) - 1):
        pos = positions[i:i+2]
        directions.append(position_pair_to_direction(pos[0], pos[1]))
    return directions

@jit(nopython=True)
def random_walk_from_directions(directions):
    START = [0,0]
    positions = [START]
    for direction in directions:
        step = polsim.step_from_direction(direction)
        positions = polsim.update_position(positions, step)
    return positions

@jit(nopython=True)
def translate_spins_to_positions(spin_system):
    splitted_spin_system = split_spins_into_pairs(spin_system)
    directions = [spin_pair_to_direction(spin_pair) for spin_pair in splitted_spin_system]
    return random_walk_from_directions(directions)

@jit(nopython=True)
def translate_positions_to_spins(positions):
    directions = positions_to_directions(positions)
    spins = []
    for direct in directions:
        spin_pair = direction_to_spin_pair(direct)
        spins.extend(spin_pair)
    return spins

def translate_position_configs_to_spins(data):
    positions_multi = data_utils.position_config_csv_to_matrix(data)
    spins_multi = []
    for positions in positions_multi:
        spins_multi.append(translate_positions_to_spins(positions))
    return spins_multi

def main():
    parser = argparse.ArgumentParser(description='Translate spin system to random walk')
    parser.add_argument('--translation',
                        default='spins_to_positions',
                        const='spins_to_positions',
                        nargs='?',
                        choices=['positions_to_spins', 'spins_to_positions', 'position_configs_to_spins'],
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
        data_utils.dump_random_walk_to_csv(args.output_file, polymer_positions)
    elif args.translation == 'positions_to_spins':
        f = open(args.input_file)
        reader = csv.reader(f)
        input_data= list(reader)
        f.close()
        positions_in = data_utils.convert_list_list_char_to_int(input_data)
        numba_positions = numba.typed.List(positions_in)
        spin_system = translate_positions_to_spins(numba_positions)
        data_utils.save_spins(spin_system, args.output_file)
    else:
        f = open(args.input_file)
        reader = csv.reader(f)
        input_data= list(reader)
        f.close()
        spin_configs = translate_position_configs_to_spins(input_data)
        data_utils.save_spin_configs(spin_configs, args.output_file)

if __name__ == "__main__":
    main()
