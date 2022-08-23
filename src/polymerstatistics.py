import polymersim as polsim
from collections import Counter

def positions_as_strings(polymer_positions):
    return [str(p) for p in polymer_positions]

def count_clashes(polymer_positions):
    count_dict = Counter(polymer_positions)
    clash_count = 0
    for key in count_dict:
        clash_check = count_dict[key]
        if clash_check > 1:
            clash_count += (clash_check - 1)
    return clash_count

random_walk = polsim.random_walk(4)
print(random_walk)
pos_as_strings = positions_as_strings(random_walk)
clashes = count_clashes(pos_as_strings)
print(clashes)
polsim.dump_random_walk_to_csv("clash_check.csv", random_walk)
