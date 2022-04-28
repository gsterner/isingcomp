import simulation_tools as sim
import math

def quencher():
    N = 196
    T_start = 0.9
    T_goal = 0.3
    Q = 10
    T_step = (T_start -T_goal) / Q
    rows = int(math.sqrt(N))
    S,J = sim.setup_nearest_neigbour_system(N, rows)
    #sim.pp_spin_system(S, rows)
    T = T_start
    for i in range(Q):
        S = sim.sweep(S, J, T)
    for i in range(2 * Q):
        T = T - T_step
        S = sim.sweep(S, J, T)
    T = T_goal
    for i in range(8 * Q):
        S = sim.sweep(S, J, T)
    sim.pp_spin_system(S, rows)
    return sim.magnetization(S)

def equilibriate(N, Q, T):
    rows = int(math.sqrt(N))
    S,J = sim.setup_nearest_neigbour_system(N, rows)
    magnetization =  []
    #sim.pp_spin_system(S, rows)
    for i in range(Q):
        S = sim.sweep(S, J, T)
        magnetization.append(sim.magnetization(S))
    #sim.pp_spin_system(S, rows)
    return magnetization
