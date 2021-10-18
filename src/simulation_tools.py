import hamiltonian as ha
import generate_system as gs
from random import random
import copy


def satisfies_boltzman_draw():
    return random() < 0.5

def is_flip_lower_energy(index, spins, spins_flip, connections):
    energy = ha.spin_hamiltonian_of_index(index, spins, connections)
    energy_flip = ha.spin_hamiltonian_of_index(index, spins_flip, connections)
    print(energy, energy_flip)
    return energy_flip < energy

def is_flip(index, spins, spins_flip, connections):
    energy = ha.spin_hamiltonian_of_index(index, spins, connections)
    energy_flip = ha.spin_hamiltonian_of_index(index, spins_flip, connections)
    if is_flip_lower_energy(index, spins, spins_flip, connections):
        return True
    elif satisfies_boltzman_draw():
        return True
    else:
        return False

def flip_spin(index, spins):
    spins_copy = copy.deepcopy(spins)
    spins_copy[index] = spins_copy[index] * -1
    return spins_copy

#TODO test this
def sim_step(spins, connections):
    #pick random site
    index = random_function(spins) #TODO implement
    #flip that spin
    spins_flip = flip_spin(index, spins)
    #check if that should be kept and update
    if is_flip(index, spins, spins_flip, connections): #TODO test is_flip function
        spins = spins_flip

S = [-1,1,1,-1]
print(S)
S_flip = flip_spin(2,S)
print(S_flip)
J = gs.create_constant_nearest_neighbour_connections(2,2,1)
print(J)
print(is_flip_lower_energy(2,S,S_flip,J))
