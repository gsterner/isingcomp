import random

# def has_right_connection(j_row, j_col, spin_dimension):
#     if j_col == spin_dimension:
#         return False
#     if (j_row + 1) == j_col:
#         return True
#     return False

# def has_left_connection(j_row, j_col, spin_dimension):
#     if j_row % spin_dimension == 0:
#         return False
#     if j_row == (j_col + 1):
#         return True
#     return False

# def has_down_connection(j_row, j_col, spin_dimension):
#     if j_row == spin_dimension:
#         return False
#     if (j_row + spin_dimension) == j_col:
#         return True
#     return False

# def has_up_connection(j_row, j_col, spin_dimension):
#     if j_row == 0:
#         return False
#     if j_row == (j_col + spin_dimension):
#         return True
#     return False

def has_right_connection(j_row, j_col, spin_dimension):
    if j_col - j_row == 1 and j_col % spin_dimension != 0:
        return True
    return False

def has_left_connection(j_row, j_col, spin_dimension):
    if j_row - j_col == 1  and j_row % spin_dimension != 0:
        return True
    return False

def has_down_connection(j_row, j_col, spin_dimension):
    if j_col - j_row == spin_dimension and j_col > spin_dimension - 1:
        return True
    return False

def has_up_connection(j_row, j_col, spin_dimension):
    if j_row -j_col == spin_dimension and j_row > spin_dimension - 1:
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

def has_periodic_right_connection(j_row, j_col, spin_dimension):
    if j_col % spin_dimension == 0 and j_row == j_col + spin_dimension - 1:
        return True
    return False

def has_periodic_left_connection(j_row, j_col, spin_dimension):
    if (j_col + 1) % spin_dimension == 0 and j_row == j_col - spin_dimension + 1:
        return True
    return False

def has_periodic_down_connection(j_row, j_col, spin_dimension):
    if j_col < spin_dimension and spin_dimension * (spin_dimension - 1) <= j_row and j_row < spin_dimension * spin_dimension and j_row - j_col == spin_dimension * (spin_dimension - 1):
        return True
    return False

def has_periodic_up_connection(j_row, j_col, spin_dimension):
    if j_row < spin_dimension and spin_dimension * (spin_dimension - 1) <= j_col and j_col < spin_dimension * spin_dimension and j_col - j_row == spin_dimension * (spin_dimension - 1):
        return True
    return False

def has_periodic_connection(j_row, j_col, spin_dimension):
    return has_periodic_right_connection(j_row, j_col, spin_dimension) or has_periodic_left_connection(j_row, j_col, spin_dimension) or has_periodic_down_connection(j_row, j_col, spin_dimension) or has_periodic_up_connection(j_row, j_col, spin_dimension)

def create_periodic_nearest_neighbour_connections(rows, cols, connection_value):
    #assume square spin matrix rows = cols
    spin_dimension = rows
    dimension = rows * cols
    connection_matrix = []
    for j_row in range(dimension):
        row_list = []
        for j_col in range(dimension):
            if has_periodic_connection(j_row, j_col, spin_dimension):
                row_list.append(connection_value)
            else:
                row_list.append(0)
        connection_matrix.append(row_list)
    return connection_matrix

def add_matrices(matrix_one, matrix_two):
    dim = len(matrix_one)
    out_matrix = []
    for r in range(dim):
        out_matrix.append([0] * dim)
    for r in range(dim):
        for c in range(dim):
            out_matrix[r][c] = matrix_one[r][c] + matrix_two[r][c]
    return out_matrix

def create_total_nearest_neighbour_connections(rows, cols, connection_value):
    nn_maxtrix = create_constant_nearest_neighbour_connections(rows, cols, connection_value)
    p_matrix = create_periodic_nearest_neighbour_connections(rows, cols, connection_value)
    return add_matrices(nn_maxtrix, p_matrix)

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

def sum_connections(connection_matrix):
    result_sum = 0
    for row in connection_matrix:
        result_sum += sum(row)
    return result_sum

def checksum_nearest_neighbour(rows):
    return 4*rows*rows - 4 * rows

def checksum_periodic_only(rows):
    return 4 * rows

def checksum_total(rows):
    return 4 * rows * rows
