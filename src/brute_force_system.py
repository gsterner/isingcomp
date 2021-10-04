import hamiltonian
import copy

spin1 = [-1, 1, 1,1]
spin2 = [1, 1, 1,1]

connections = [[4, 0, -4, 0],
               [0, 4, 0, -4],
               [-4, 0, 4, 0],
               [0, -4, 0, 4]]

def generate_children_at_position(config, position):
    neg_config = copy.deepcopy(config)
    neg_config[position] = -1
    pos_config = copy.deepcopy(config)
    pos_config[position] = 1
    return [neg_config, pos_config]

def generate_children_current_config_at_position(configs, position):
    out_configs = []
    for config in configs:
        out_configs.extend(generate_children_at_position(config, position))
    return out_configs

print(generate_children_current_config_at_position([spin1,spin2], 1))
