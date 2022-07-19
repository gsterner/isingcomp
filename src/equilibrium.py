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

def main():
    parser = argparse.ArgumentParser(description='Run ising equilibrium from input file')
    parser.add_argument('system_file', metavar='system_file', type=str, help='System File')
    parser.add_argument('sweeps_to_equilibrium', metavar='sweeps_to_equilibrium', type=int, help='Number of sweeps to reach equilibrium')
    parser.add_argument('temperature', metavar='temperature', type=float, help='Temperature')
    args = parser.parse_args()
    f_sys = open(args.system_file)
    system = json.load(f_sys)
    f_sys.close()

    spins = equilibrium(system["spins"],
                        system["connections"],
                        args.sweeps_to_equilibrium,
                        args.temperature)
    print(args.temperature, sim.magnetization(spins))

if __name__ == "__main__":
    main()
