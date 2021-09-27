import sys
sys.path.append('../src')
import hamiltonian


def test_hamiltionian_all_twos():
    spins = [-1, 1, 1,1]
    connections = [[2, 2, 2, 2],
                   [2, 2, 2, 2],
                   [2, 2, 2, 2],
                   [2, 2, 2, 2]]
    assert hamiltonian.spin_hamiltonian_of_index(0, spins, connections) == -4

def test_up_up_up_up_first_spin():
    spins = [1, 1, 1,1]
    connections = [[4, 0, -4, 0],
                   [0, 4, 0, -4],
                   [-4, 0, 4, 0],
                   [0, -4, 0, 4]]
    assert hamiltonian.spin_hamiltonian_of_index(0, spins, connections) == 0

def test_up_up_up_up_system():
    spins = [1, 1, 1,1]
    connections = [[4, 0, -4, 0],
                   [0, 4, 0, -4],
                   [-4, 0, 4, 0],
                   [0, -4, 0, 4]]
    assert hamiltonian.hamiltonian_of_system(spins, connections) == 0

def test_up_up_down_down_first_spin():
    spins = [1, 1, -1, -1]
    connections = [[4, 0, -4, 0],
                   [0, 4, 0, -4],
                   [-4, 0, 4, 0],
                   [0, -4, 0, 4]]
    assert hamiltonian.spin_hamiltonian_of_index(0, spins, connections) == 8

def test_up_up_down_down_system():
    spins = [1, 1, -1, -1]
    connections = [[4, 0, -4, 0],
                   [0, 4, 0, -4],
                   [-4, 0, 4, 0],
                   [0, -4, 0, 4]]
    assert hamiltonian.hamiltonian_of_system(spins, connections) == 32
