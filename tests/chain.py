import sys
sys.path.append('../src')
import systemdata
import grid

DATA_FOLDER = '../data/'
SPIN_DATA_CHAIN_CHECK = 'chain_check.json'

def spin_data_chain_check():
    return DATA_FOLDER + SPIN_DATA_CHAIN_CHECK

def test_spin_data_first_entry():
    system_data = systemdata.SystemData(spin_data_chain_check())
    assert system_data.spins[0][0] == -1

def test_connection_data_first_entry():
    system_data = systemdata.SystemData(spin_data_chain_check())
    assert system_data.connections[0][0] == 2

def test_spin_data_dimension_row():
    system_data = systemdata.SystemData(spin_data_chain_check())
    assert len(system_data.spins) == 1

def test_spin_data_dimension_column():
    system_data = systemdata.SystemData(spin_data_chain_check())
    assert len(system_data.spins[0]) == 4

def test_connection_data_dimension_row():
    system_data = systemdata.SystemData(spin_data_chain_check())
    assert len(system_data.connections) == 4

def test_connection_data_dimension_column():
    system_data = systemdata.SystemData(spin_data_chain_check())
    assert len(system_data.connections[0]) == 4

def test_grid_get_spin_matrix():
    system_data = systemdata.SystemData(spin_data_chain_check())
    current_grid = grid.Grid(system_data)
    assert current_grid.get_spin_matrix() == system_data.spins
