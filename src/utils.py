import json

def save_spins(spins, file_name):
    out_dict = {"spins":spins}
    with open(file_name, 'w') as f:
        json.dump(out_dict, f)
        f.close()

def save_connections(connections, file_name):
    out_dict = {"connections":connections}
    with open(file_name, 'w') as f:
        json.dump(out_dict, f)
        f.close()
