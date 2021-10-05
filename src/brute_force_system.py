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

def add_element(config):
    neg_config = copy.deepcopy(config)
    neg_config.append(-1)
    pos_config = copy.deepcopy(config)
    pos_config.append(1)
    return [neg_config, pos_config]

def generate_children_current_config_at_position(configs, position):
    out_configs = []
    for config in configs:
        out_configs.extend(generate_children_at_position(config, position))
    return out_configs

config = [[]]
for index in range(3):
    config_list = [add_element(current_config) for current_config in config]
    print(config_list)
    config = [val for sublist in config_list for val in sublist]
    print(config)
