import hamiltonian as ha
from random import random
import copy

#testing
def satisfies_boltzman_draw():
    return random < 0.5

def is_flip(index, spins, spins_flip, connections):
    energy = ha.spin_hamiltonian_of_index(index, spins, connections)
    energy_flip = ha.spin_hamiltonian_of_index(index, spins_flip, connections)
    if energy < energy_flip:
        return True
    elif satisfies_boltzman_draw():
        return True
    else:
        return False

def flip_spin(index, spins):
    spins_copy = copy.deepcopy(spins)
    spins_copy[index] = spins_copy[index] * -1
    return spins_copy

spins = [1,1,1,1]
print(spins)
spins_flip = flip_spin(2,spins)
print(spins)
print(spins_flip)
