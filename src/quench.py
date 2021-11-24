import simulation_tools as sim
import math

def percent(part, full):
    return str(part/full * 100) + "%"

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

def simple():
    N = 196
    Q = 110
    T = 0.3
    rows = int(math.sqrt(N))
    S,J = sim.setup_nearest_neigbour_system(N, rows)
    #sim.pp_spin_system(S, rows)
    for i in range(Q):
        S = sim.sweep(S, J, T)
    sim.pp_spin_system(S, rows)
    return sim.magnetization(S)

def simulation():
    SIMS = 20
    magnetization = []
    for s in range(SIMS):
        m = simple()
        #m = quencher()
        print(percent(s, SIMS))
        magnetization.append(m)
    return magnetization

magnet = simulation()
abs_magnet = [abs(m) for m in magnet]
print(magnet)
print(abs_magnet)
print(sum(magnet), sum(abs_magnet), sum(magnet)/len(magnet), sum(abs_magnet)/len(abs_magnet))
