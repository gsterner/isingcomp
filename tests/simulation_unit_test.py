import sys
sys.path.append('../src')
import simulation_tools
import generate_system

def test_satisfies_boltzman_draw():
    draw = simulation_tools.satisfies_boltzman_draw()
    assert draw == True or draw == False

def test_flip_spin():
    S = [1,1,1,1]
    S_flip = simulation_tools.flip_spin(2,S)
    expected_flip = [1,1,-1,1]
    assert S_flip == expected_flip

def test_is_flip_lower_energy():
    S = [1,1,1,1]
    S_flip = simulation_tools.flip_spin(2,S)
    J = generate_system.create_constant_nearest_neighbour_connections(2,2,1)
    assert simulation_tools.is_flip_lower_energy(2,S,S_flip,J) == False

def test_is_flip():
    S = [1,1,1,1]
    S_flip = simulation_tools.flip_spin(2,S)
    J = generate_system.create_constant_nearest_neighbour_connections(2,2,1)
    is_flip_val = simulation_tools.is_flip(2, S, S_flip, J)
    assert is_flip_val == True or is_flip_val == False

def test_randomize_index():
    S = [1,1,1,1]
    random_number = simulation_tools.randomize_index(S)
    assert random_number >= 0 and random_number < len(S)
    assert type(random_number) == type(int())

def test_sim_step():
    S = [-1,1,1,-1]
    J = generate_system.create_constant_nearest_neighbour_connections(2,2,1)
    S_step = simulation_tools.sim_step(S, J)
    assert S_step != S
