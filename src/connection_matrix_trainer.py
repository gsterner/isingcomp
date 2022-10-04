import polymersim as poly
import system_translation as systrans
import connection_matrix_creation as cmc
import polymerstatistics as polstat
import numpy as np
from numpy import linalg

walk_length = 5
spin_dim = 2 * walk_length
no_test_walks = 10000
connections_total = np.zeros((spin_dim, spin_dim))
unallowed_count = 0

#why does it work with 4 but not the others???

#Find a way to skip those that have already been done???
unallowed_walks = set()
for i in range(no_test_walks):
    polymer_positions = poly.random_walk(walk_length)
    is_unallowed = polstat.has_duplicates(polymer_positions)
    if is_unallowed and polymer_positions.__str__() not in unallowed_walks:
        unallowed_walks.add(polymer_positions.__str__())
        spin_system = systrans.translate_positions_to_spins(polymer_positions)
        connections = cmc.outer_square(spin_system)
        connections_total += connections
        unallowed_count += 1

for walk in unallowed_walks:
    print(walk)

print(connections_total)
connections_total = connections_total / unallowed_count
print("unalllowed",unallowed_count)
print("norm", linalg.norm(connections_total))
print(connections_total)
true_4 = np.array([
    [-4, 0, 4, 0],
    [0, -4, 0, 4],
    [4, 0, -4, 0],
    [0, 4, 0, -4]
])
true_4 = true_4 / 4
print("true 4 norm", linalg.norm(true_4))
print(true_4)

true_6 = np.array([
    [-6, 0, 6, 0, 0, 0],
    [0, -6, 0, 6, 0, 0],
    [6, 0, -6, 0, 6, 0],
    [0, 6, 0, -6, 0, 6],
    [0, 0, 6, 0, -6, 0],
    [0, 0, 0, 6, 0, -6]
])
true_6 = true_6 / 6
print("true 6 norm", linalg.norm(true_6))

true_10 = np.array([[-1004476, 0, 15484, 0, 8484, 0, 4284, 0, 3932, 0, 2492, 0, 1980, 0, 1108, 0, 732, 0, 196, 0], [0, -1004476, 0, 15484, 0, 8484, 0, 4284, 0, 3932, 0, 2492, 0, 1980, 0, 1108, 0, 732, 0, 196], [15484, 0, -1004476, 0, 16396, 0, 12340, 0, 7236, 0, 5668, 0, 4020, 0, 2748, 0, 1684, 0, 732, 0], [0, 15484, 0, -1004476, 0, 16396, 0, 12340, 0, 7236, 0, 5668, 0, 4020, 0, 2748, 0, 1684, 0, 732], [8484, 0, 16396, 0, -1004476, 0, 17612, 0, 12684, 0, 8588, 0, 6508, 0, 4356, 0, 2748, 0, 1108, 0], [0, 8484, 0, 16396, 0, -1004476, 0, 17612, 0, 12684, 0, 8588, 0, 6508, 0, 4356, 0, 2748, 0, 1108], [4284, 0, 12340, 0, 17612, 0, -1004476, 0, 17396, 0, 13236, 0, 8580, 0, 6508, 0, 4020, 0, 1980, 0], [0, 4284, 0, 12340, 0, 17612, 0, -1004476, 0, 17396, 0, 13236, 0, 8580, 0, 6508, 0, 4020, 0, 1980], [3932, 0, 7236, 0, 12684, 0, 17396, 0, -1004476, 0, 17476, 0, 13236, 0, 8588, 0, 5668, 0, 2492, 0], [0, 3932, 0, 7236, 0, 12684, 0, 17396, 0, -1004476, 0, 17476, 0, 13236, 0, 8588, 0, 5668, 0, 2492], [2492, 0, 5668, 0, 8588, 0, 13236, 0, 17476, 0, -1004476, 0, 17396, 0, 12684, 0, 7236, 0, 3932, 0], [0, 2492, 0, 5668, 0, 8588, 0, 13236, 0, 17476, 0, -1004476, 0, 17396, 0, 12684, 0, 7236, 0, 3932], [1980, 0, 4020, 0, 6508, 0, 8580, 0, 13236, 0, 17396, 0, -1004476, 0, 17612, 0, 12340, 0, 4284, 0], [0, 1980, 0, 4020, 0, 6508, 0, 8580, 0, 13236, 0, 17396, 0, -1004476, 0, 17612, 0, 12340, 0, 4284], [1108, 0, 2748, 0, 4356, 0, 6508, 0, 8588, 0, 12684, 0, 17612, 0, -1004476, 0, 16396, 0, 8484, 0], [0, 1108, 0, 2748, 0, 4356, 0, 6508, 0, 8588, 0, 12684, 0, 17612, 0, -1004476, 0, 16396, 0, 8484], [732, 0, 1684, 0, 2748, 0, 4020, 0, 5668, 0, 7236, 0, 12340, 0, 16396, 0, -1004476, 0, 15484, 0], [0, 732, 0, 1684, 0, 2748, 0, 4020, 0, 5668, 0, 7236, 0, 12340, 0, 16396, 0, -1004476, 0, 15484], [196, 0, 732, 0, 1108, 0, 1980, 0, 2492, 0, 3932, 0, 4284, 0, 8484, 0, 15484, 0, -1004476, 0], [0, 196, 0, 732, 0, 1108, 0, 1980, 0, 2492, 0, 3932, 0, 4284, 0, 8484, 0, 15484, 0, -1004476]])

true_10 = true_10 / 1004476
print("true unallowed", 1004476)
print("true norm", linalg.norm(true_10))
