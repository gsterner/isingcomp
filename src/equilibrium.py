import simulation_tools as sim

def equilibriate(S, J, Q, T):
    #S,J = sim.setup_nearest_neigbour_system(N, int(math.sqrt(N)))
    #rows = int(math.sqrt(len(S)))
    magnetization =  []
    #sim.pp_spin_system(S, rows)
    for i in range(Q):
        S = sim.sweep(S, J, T)
        magnetization.append(sim.magnetization(S))
    #sim.pp_spin_system(S, rows)
    return magnetization
