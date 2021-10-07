def spin_hamiltonian(spin, all_spins, spin_connections):
    return spin * sum(i[0] * i[1] for i in zip(all_spins, spin_connections))

def spin_hamiltonian_of_index(index, spins, connections):
    return spin_hamiltonian(spins[index], spins, connections[index])

def hamiltonian_of_system(spins, connections):
    energy = 0
    for index in range(len(spins)):
        energy += spin_hamiltonian_of_index(index, spins, connections)
    return energy
