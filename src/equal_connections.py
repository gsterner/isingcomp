import data_utils
import numpy as np
import argparse

def equal_connections(matrix_dim):
    connections = np.ones((matrix_dim, matrix_dim))
    connections = connections.astype(int)
    return connections.tolist()

def minus_connections(matrix_dim):
    connections = np.ones((matrix_dim, matrix_dim)) * -1
    connections = connections.astype(int)
    return connections.tolist()

def random_connections(matrix_dim):
    connections = np.random.randn(matrix_dim, matrix_dim)
    return connections.tolist()

def zero_connections(matrix_dim):
    connections = np.zeros((matrix_dim, matrix_dim))
    connections = connections.astype(int)
    return connections.tolist()

def banded_connections(matrix_dim):
    connections = np.ones((matrix_dim, matrix_dim))
    connections = connections.astype(int)
    for di in range(matrix_dim):
        for du in range(matrix_dim):
            if (di + du) %  2 != 0:
                connections[di, du] = 0
    print(connections)
    return connections.tolist()

def main():
    parser = argparse.ArgumentParser(description='Create connection matrix with equal weights')
    parser.add_argument('matrix_dim',
                        metavar='matrix_dim',
                        type=int,
                        help='Matrix dimension')

    args = parser.parse_args()
    #connections = equal_connections(args.matrix_dim)
    connections = banded_connections(args.matrix_dim)
    data_utils.save_connections(connections, "banded_connections.json")

if __name__ == "__main__":
    main()
