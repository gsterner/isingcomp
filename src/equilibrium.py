import simulation_tools as sim
import argparse
import json

def equilibrium(spins_in, connections, sweeps, temperature):
    spins = spins_in
    for i in range(sweeps):
        spins = sim.sweep(spins, connections, temperature)
    return spins

#TODO clean this function up. change name and variables. should magnetization be calculated like this???
def equilibriate(S, J, Q, T):
    magnetization =  []
    for i in range(Q):
        S = sim.sweep(S, J, T)
        magnetization.append(sim.magnetization(S))
    return magnetization

def save_spins(spins, file_name):
    out_dict = {"spins":spins}
    with open(file_name, 'w') as f:
        json.dump(out_dict, f)
        f.close()

def main():
    parser = argparse.ArgumentParser(description='Run ising equilibrium from input files')
    parser.add_argument('spin_file', metavar='spin_file', type=str, help='Spin File')
    parser.add_argument('connection_file', metavar='connection_file', type=str, help='Connection File')
    parser.add_argument('sweeps_to_equilibrium', metavar='sweeps_to_equilibrium', type=int, help='Number of sweeps to reach equilibrium')
    parser.add_argument('temperature', metavar='temperature', type=float, help='Temperature')
    args = parser.parse_args()
    f_spins = open(args.spin_file)
    spins = json.load(f_spins)
    f_spins.close()
    f_connections = open(args.connection_file)
    connections = json.load(f_connections)
    f_connections.close()

    equilibrium_spins = equilibrium(spins["spins"],
                                    connections["connections"],
                                    args.sweeps_to_equilibrium,
                                    args.temperature)
    save_spins(equilibrium_spins, "spins_output.json")
    print(args.temperature, sim.magnetization(equilibrium_spins))

if __name__ == "__main__":
    main()
