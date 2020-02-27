import json


def get_json_data(file_path):
    with open(file_path) as json_file:
        return json.load(json_file)

class SystemData:
    
    def __init__(self, file_path):
        json_data = get_json_data(file_path)
        self.spins = json_data["spins"]
        self.connections = json_data["connections"]
