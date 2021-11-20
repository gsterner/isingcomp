import simulation_tools as sim
import math

N = 400
T_start = 0.5
T_goal = 0.01
Q = 300
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
