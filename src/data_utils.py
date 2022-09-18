import json
import csv

def save_spins(spins, file_name):
    out_dict = {"spins":spins}
    with open(file_name, 'w') as f:
        json.dump(out_dict, f)
        f.close()

def save_spin_configs(spin_configs_raw, file_name):
    spin_configs = []
    for config in spin_configs_raw:
        spin_configs.append({"spins":config})
    out_dict = {"spin_configs":spin_configs}
    with open(file_name, 'w') as f:
        json.dump(out_dict, f)
        f.close()

def save_connections(connections, file_name):
    out_dict = {"connections":connections}
    with open(file_name, 'w') as f:
        json.dump(out_dict, f)
        f.close()

def dump_random_walk_to_csv(file_name, polymer_positions):
    with open(file_name, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(polymer_positions)
