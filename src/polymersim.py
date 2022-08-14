import enum
import random
import csv
import argparse

CLASH = "CLASH"

class Direction(enum.Enum):
    NORTH = enum.auto()
    SOUTH = enum.auto()
    EAST  = enum.auto()
    WEST  = enum.auto()

def direction_from_rand(rand_nr):
    if rand_nr < 0.25:
        return Direction.NORTH
    if rand_nr < 0.5:
        return Direction.SOUTH
    if rand_nr < 0.75:
        return Direction.EAST
    return Direction.WEST

def step_from_direction(direction_in):
    if direction_in == Direction.NORTH:
        return [0,1]
    if direction_in == Direction.SOUTH:
        return [0,-1]
    if direction_in == Direction.EAST:
        return [1, 0]
    return [-1, 0]

def update_position(position_list, step):
    current_position = position_list[-1]
    new_position = [current_position[0] + step[0], current_position[1] + step[1]]
    position_list.append(new_position)
    return position_list

def update_position_self_avoiding(position_list, step):
    current_position = position_list[-1]
    new_position = [current_position[0] + step[0], current_position[1] + step[1]]
    if new_position in position_list:
        return CLASH
    position_list.append(new_position)
    return position_list

def random_walk(number_of_steps):
    START = [0,0]
    positions = [START]
    for number in range(number_of_steps):
        random_number = random.random()
        direction = direction_from_rand(random_number)
        step = step_from_direction(direction)
        positions = update_position(positions, step)
    return positions

def self_avoiding_random_walk(number_of_steps):
    START = [0,0]
    positions = [START]
    for number in range(number_of_steps):
        random_number = random.random()
        direction = direction_from_rand(random_number)
        step = step_from_direction(direction)
        update = update_position_self_avoiding(positions, step)
        if update == CLASH:
            return positions
        else:
            positions = update
    return positions

def self_avoiding_random_walk_complete(number_of_steps):
    polymer_positions = []
    tries = 0
    while len(polymer_positions) < number_of_steps:
        polymer_positions = self_avoiding_random_walk(number_of_steps)
        tries += 1
        #print('length', len(polymer_positions))
    print("Number of tries:", tries)
    return polymer_positions

#TODO clean up interface so that type of walk can be configured, and number of steps parameter. Also clean up functions and remove duplicated code.
def main():
    parser = argparse.ArgumentParser(description='Run polymersimulation')
    parser.add_argument('output_file', metavar='output_file', type=str, help='Output File')
    parser.add_argument('number_steps', metavar='number_steps', type=int, help='Number of Steps')
    args = parser.parse_args()

    polymer_positions = self_avoiding_random_walk_complete(args.number_steps)
    with open(args.output_file, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(polymer_positions)

if __name__ == "__main__":
    main()
