import polymersim as polsim
from collections import Counter
from numba import jit
import numpy as np

@jit(nopython=True)
def has_duplicates(positions):
    positions_left = positions[1:]
    for pos in positions:
        if pos in positions_left:
            return True
        positions_left = positions_left[1:]
    return False

def positions_as_strings(polymer_positions):
    return [str(p) for p in polymer_positions]

def count_clashes_strings(polymer_positions_strings):
    count_dict = Counter(polymer_positions_strings)
    clash_count = 0
    for key in count_dict:
        clash_check = count_dict[key]
        if clash_check > 1:
            clash_count += (clash_check - 1)
    return clash_count

def count_clashes(polymer_positions):
    polymer_positions_strings = positions_as_strings(polymer_positions)
    return count_clashes_strings(polymer_positions_strings)

def root_mean_square(polymer_positions):
    pos = np.array(polymer_positions)
    return np.sqrt(np.mean(pos**2))

# random_walk = polsim.random_walk(4)
# print(random_walk)
# pos_as_strings = positions_as_strings(random_walk)
# clashes = count_clashes(pos_as_strings)
# print(clashes)
# polsim.dump_random_walk_to_csv("clash_check.csv", random_walk)
