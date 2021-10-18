import random

def has_right_connection(j_row, j_col, spin_dimension):
    if j_col == spin_dimension:
        return False
    if (j_row + 1) == j_col:
        return True
    return False

def has_left_connection(j_row, j_col, spin_dimension):
    if j_row % spin_dimension == 0:
        return False
    if j_row == (j_col + 1):
        return True
    return False

def has_down_connection(j_row, j_col, spin_dimension):
    if j_row == spin_dimension:
        return False
    if (j_row + spin_dimension) == j_col:
        return True
    return False

def has_up_connection(j_row, j_col, spin_dimension):
    if j_row == 0:
        return False
    if j_row == (j_col + spin_dimension):
        return True
    return False

def has_connection(j_row, j_col, spin_dimension):
    return has_right_connection(j_row, j_col, spin_dimension) or has_left_connection(j_row, j_col, spin_dimension) or has_down_connection(j_row, j_col, spin_dimension) or has_up_connection(j_row, j_col, spin_dimension)

    #2D Symmetric connection square system non-periodic
def create_constant_nearest_neighbour_connections(rows, cols, connection_value):
    #assume square spin matrix rows = cols
    spin_dimension = rows
    dimension = rows * cols
    connection_matrix = []
    for j_row in range(dimension):
        row_list = []
        for j_col in range(dimension):
            if has_connection(j_row, j_col, spin_dimension):
                row_list.append(connection_value)
            else:
                row_list.append(0)
        connection_matrix.append(row_list)
    return connection_matrix

def pp_connection_matrix(connection_matrix):
    for j_row_list in connection_matrix:
        print(j_row_list)

def random_spin():
    if random.random() < 0.5:
        return -1
    else:
        return 1

def create_randomized_spins(size):
    spin_list = [random_spin() for spin in range(size)]
    return spin_list
