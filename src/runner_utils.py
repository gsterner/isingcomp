import equilibrium as equilib
import simulation_tools as sim
import math

def percent(part, full):
    return str(part/full * 100) + "%"

def simulation(N, Q, T, SIMS):
    #SIMS = 1
    S,J = sim.setup_nearest_neigbour_system(N, int(math.sqrt(N)))
    magnetization = []
    for s in range(SIMS):
        m = equilib.equilibriate(S, J, Q, T)
        #print(percent(s, SIMS))
        magnetization.append(m)
    return magnetization

def calc_abs_magnetization(magnet, cut_off_fraction):
    abs_magnet = [abs(m) for m in magnet]
    cutoff = int(cut_off_fraction * len(abs_magnet))
    cut_off_magnet = abs_magnet[cutoff:]
    return sum(cut_off_magnet)/len(cut_off_magnet)

def mean_over_simulations(N, Q, T, sims, cut_off_fraction):
    M = simulation(N, Q, T, sims)
    abs_m = []
    for m in M:
        abs_m.append(calc_abs_magnetization(m, cut_off_fraction))
    return sum(abs_m)/len(abs_m)
