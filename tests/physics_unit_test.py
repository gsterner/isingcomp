import sys
sys.path.append('../src')
import hamiltonian
import generate_system

def test_hamiltionian_all_twos():
    spins = [-1, 1, 1,1]
    connections = [[2, 2, 2, 2],
                   [2, 2, 2, 2],
                   [2, 2, 2, 2],
                   [2, 2, 2, 2]]
    assert hamiltonian.spin_hamiltonian_of_index(0, spins, connections) == 4

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
    assert hamiltonian.spin_hamiltonian_of_index(0, spins, connections) == -8

def test_up_up_down_down_system():
    spins = [1, 1, -1, -1]
    connections = [[4, 0, -4, 0],
                   [0, 4, 0, -4],
                   [-4, 0, 4, 0],
                   [0, -4, 0, 4]]
    assert hamiltonian.hamiltonian_of_system(spins, connections) == -32

def test_generate_nearest_neighbour_connections():
    expected_connections = [[0, 1, 1, 0],
                            [1, 0, 0, 1],
                            [1, 0, 0, 1],
                            [0, 1, 1, 0]]
    connections = generate_system.create_constant_nearest_neighbour_connections(2,2,1)
    assert connections == expected_connections

def test_generate_nearest_neighbour_connections():
    expected_connections = [[0, 1, 1, 0],
                            [1, 0, 0, 1],
                            [1, 0, 0, 1],
                            [0, 1, 1, 0]]
    connections = generate_system.create_periodic_nearest_neighbour_connections(2,2,1)
    generate_system.pp_connection_matrix(connections)

connections = generate_system.create_periodic_nearest_neighbour_connections(3,3,1)
generate_system.pp_connection_matrix(connections)
