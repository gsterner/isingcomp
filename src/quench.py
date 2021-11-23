import simulation_tools as sim
import math

def quencher():
    N = 400
    T_start = 0.5
    T_goal = 0.01
    Q = 10
    T_step = (T_start -T_goal) / Q
    rows = int(math.sqrt(N))
    S,J = sim.setup_nearest_neigbour_system(N, rows)
    sim.pp_spin_system(S, rows)
    T = T_start
    for i in range(Q):
        S = sim.sweep(S, J, T)
        #sim.pp_spin_system(S, rows)
        #print(i, sim.magnetization(S))
    sim.pp_spin_system(S, rows)
    print(i, sim.magnetization(S))
    for i in range(Q):
        T = T - T_step
        S = sim.sweep(S, J, T)
        #sim.pp_spin_system(S, rows)
        #print(i, T,  sim.magnetization(S))
    sim.pp_spin_system(S, rows)
    print(i, T,  sim.magnetization(S))
    T = T_goal
    for i in range(Q):
        S = sim.sweep(S, J, T)
        #sim.pp_spin_system(S, rows)
        #print(i, sim.magnetization(S))
    sim.pp_spin_system(S, rows)
    print(i, T,  sim.magnetization(S))

def percent(part, full):
    return str(part/full * 100) + "%"

def simple():
    N = 100
    Q = 10
    T = 0.3
    rows = int(math.sqrt(N))
    S,J = sim.setup_nearest_neigbour_system(N, rows)
    #sim.pp_spin_system(S, rows)
    for i in range(Q):
        S = sim.sweep(S, J, T)
    #sim.pp_spin_system(S, rows)
    return sim.magnetization(S)

SIMS = 50
magnet = []
for s in range(SIMS):
    m = simple()
    print(percent(s, SIMS))
    magnet.append(m)

abs_magnet = [abs(m) for m in magnet]
print(magnet)
print(abs_magnet)
print(sum(magnet), sum(abs_magnet), sum(magnet)/len(magnet), sum(abs_magnet)/len(abs_magnet))
