import utils
import numpy as np
import argparse
import json

def outer_square(spins_np):
    return np.outer(spins_np, spins_np)

def estimate_connections(spins):
    spins_np = np.array(spins)
    connections_np = outer_square(spins_np)
    return connections_np.tolist()

def main():
    parser = argparse.ArgumentParser(description='Create connection matrix that maximises cost for spin config')
    parser.add_argument('spin_file', metavar='spin_file', type=str, help='Spin File')
    args = parser.parse_args()
    f_spins = open(args.spin_file)
    spins = json.load(f_spins)
    f_spins.close()
    connections = estimate_connections(spins["spins"])
    utils.save_connections(connections, "connections_output.json")

if __name__ == "__main__":
    main()
