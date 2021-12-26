import simulation_tools as sim
import math
import pylab as pl

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

def simple(N, Q, T):
    # N = 256
    # Q = 5000
    # T = 0.11
    rows = int(math.sqrt(N))
    S,J = sim.setup_nearest_neigbour_system(N, rows)
    magnetization =  []
    #sim.pp_spin_system(S, rows)
    for i in range(Q):
        S = sim.sweep(S, J, T)
        magnetization.append(sim.magnetization(S))
        #print(percent(i, Q))
    #sim.pp_spin_system(S, rows)
    return magnetization

def simulation(N, Q, T, SIMS):
    #SIMS = 1
    magnetization = []
    for s in range(SIMS):
        m = simple(N, Q, T)
        #m = quencher()
        #print(percent(s, SIMS))
        magnetization.append(m)
    return magnetization

def calc_abs_magnetization(magnet, cutoff):
    abs_magnet = [abs(m) for m in magnet]
    cut_off_magnet = abs_magnet[cutoff:]
    return sum(cut_off_magnet)/len(cut_off_magnet)

def mean_over_simulations(N, Q, T, sims, cut_off):
    M = simulation(N, Q, T, sims)
    abs_m = []
    for m in M:
        abs_m.append(calc_abs_magnetization(m, cut_off))
    return sum(abs_m)/len(abs_m)

def pre_analyze(N, Q, T):
    magnet = simulation(N, Q, T, 1)[0]
    abs_magnet = [abs(m) for m in magnet]
    pl.subplot(2,1,1)
    pl.plot(magnet)
    pl.subplot(2,1,2)
    pl.plot(abs_magnet)
    pl.show()
    #print(abs_magnet)
    print(sum(magnet), sum(abs_magnet), sum(magnet)/len(magnet), sum(abs_magnet)/len(abs_magnet))

#pre_analyze(100, 1000, 0.01)
temperatures = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16]
magnets = []
for temp in temperatures:
    print(temp)
    magnets.append(mean_over_simulations(144, 1000, temp, 10, 600))

print(magnets)
pl.plot(temperatures, magnets)
pl.show()
