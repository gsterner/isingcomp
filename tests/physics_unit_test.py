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

def test_spin_sum_nearest_neighbour_connections():
    rows = 5
    connections_nn = generate_system.create_constant_nearest_neighbour_connections(rows, rows, 1)
    calc_sum = generate_system.sum_connections(connections_nn)
    check_sum = generate_system.checksum_nearest_neighbour(rows)
    assert calc_sum == check_sum

def test_spin_sum_nearest_neighbour_periodic_connections():
    rows = 5
    connections_p = generate_system.create_periodic_nearest_neighbour_connections(rows, rows, 1)
    calc_sum = generate_system.sum_connections(connections_p)
    check_sum = generate_system.checksum_periodic_only(rows)
    assert calc_sum == check_sum

def test_spin_sum_total_connections():
    rows = 5
    connections_t = generate_system.create_total_nearest_neighbour_connections(rows, rows, 1)
    calc_sum = generate_system.sum_connections(connections_t)
    check_sum = generate_system.checksum_total(rows)
    assert calc_sum == check_sum
