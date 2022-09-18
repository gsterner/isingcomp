import simulation_tools
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

def order_postions(positions_raw):
    number_of_configs = int(len(positions_raw[0])/2)
    grouped_rows = []
    for pos in positions_raw:
        grouped_rows.append(list(simulation_tools.chunker(pos,2)))
    positions_ordered = []
    for config in range(number_of_configs):
        config_positions = []
        for row in grouped_rows:
            config_positions.append(row[config])
        positions_ordered.append(config_positions)
    return positions_ordered

def convert_list_list_char_to_int(outer_list):
    return [[int(char_element) for char_element in inner_list] for inner_list in outer_list]

def position_config_csv_to_matrix(position_configs_csv):
    positions_raw = convert_list_list_char_to_int(position_configs_csv)
    positions_multi = order_postions(positions_raw)
    return positions_multi

def pick_row(row_index, position_configs):
    row = []
    for config in position_configs:
        row.extend(config[row_index])
    return row

def order_positions_columnwise(position_config_matrix):
    polymer_length = int(len(position_config_matrix[0]))
    positions_rows = []
    for pos_index in range(polymer_length):
        positions_rows.append(pick_row(pos_index, position_config_matrix))
    return positions_rows
