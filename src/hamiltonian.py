import argparse
import systemdata

def spin_hamiltonian(spin, all_spins, spin_connections):
    print(all_spins)
    return spin * sum(i[0] * i[1] for i in zip(all_spins, spin_connections))

def spin_hamiltonian_of_index(index, spins, connections):
    return spin_hamiltonian(spins[index], spins, connections[index])

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
system_data = systemdata.SystemData(args.filename)
print(spin_hamiltonian_of_index(0, system_data.spins[0], system_data.connections))
