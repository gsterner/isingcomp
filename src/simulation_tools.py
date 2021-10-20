import hamiltonian as ha
import generate_system as gs
import random
import copy
import math

def satisfies_boltzman_draw(temperature):
    return random.random() < temperature

def is_flip_lower_energy(index, spins, spins_flip, connections):
    energy = ha.spin_hamiltonian_of_index(index, spins, connections)
    energy_flip = ha.spin_hamiltonian_of_index(index, spins_flip, connections)
    return energy_flip < energy

def is_flip(index, spins, spins_flip, connections, temperature):
    energy = ha.spin_hamiltonian_of_index(index, spins, connections)
    energy_flip = ha.spin_hamiltonian_of_index(index, spins_flip, connections)
    if is_flip_lower_energy(index, spins, spins_flip, connections):
        return True
    elif satisfies_boltzman_draw(temperature):
        return True
    else:
        return False

def flip_spin(index, spins):
    spins_copy = copy.deepcopy(spins)
    spins_copy[index] = spins_copy[index] * -1
    return spins_copy

def randomize_index(spins):
    return random.randint(0, len(spins) - 1)

def sim_step(spins, connections, temperature):
    #pick random site
    index = randomize_index(spins)
    #flip that spin
    spins_flip = flip_spin(index, spins)
    #check if that should be kept and update
    is_flip_val = is_flip(index, spins, spins_flip, connections, temperature)
    #print("flip", is_flip_val, spins_flip)
    if is_flip_val:
        return spins_flip
    else:
        return spins

def sweep(spins, connections, temperature):
    for i in range(len(spins)):
        spins = sim_step(spins, connections, temperature)
    return spins

def spin_to_char(spin):
    if spin == -1:
        return '-'
    else:
        return '+'

def setup_nearest_neigbour_system(system_size, rows):
    spins = gs.create_randomized_spins(system_size)
    connections = gs.create_constant_nearest_neighbour_connections(rows, rows, 1)
    return spins, connections

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))

def pp_spin_system(spins, row_size):
    spins_as_chars = [spin_to_char(spin) for spin in spins]
    for row in chunker(spins_as_chars, row_size):
        print(''.join(row))

#######################
N = 900
T = 0.1
rows = int(math.sqrt(N))
S,J = setup_nearest_neigbour_system(N, rows)
pp_spin_system(S, rows)
print('_'*rows)
for i in range(100):
    S = sweep(S, J, T)
    pp_spin_system(S, rows)
    print('_'*rows, sum(S))
