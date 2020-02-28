import argparse
import systemdata
import vertex
import json

class Grid:

    def __init__(self, system_data):
        spin_matrix = system_data.spins
        self.rows = len(spin_matrix)
        self.columns = len(spin_matrix[0])
        self.vertices = make_vertices(spin_matrix)

    def get_spin_matrix(self):
        spin_matrix = []
        for row in range(self.rows):
            spin_matrix.append([None] * self.columns)
        for v in self.vertices:
            spin_matrix[v.row][v.column] = v.spin_value
        return spin_matrix

def make_vertices(spin_matrix):
    rows = len(spin_matrix)
    columns = len(spin_matrix[0])
    vertices = []
    for row in range(rows):
        for column in range(columns):
            current_vertex = vertex.Vertex(spin_matrix[row][column], None, [row, column])
            vertices.append(current_vertex)
    return vertices

# parser = argparse.ArgumentParser()
# parser.add_argument('filename')
# args = parser.parse_args()
# system_data = systemdata.SystemData(args.filename)
# grid = Grid(system_data)
# print(json.dumps(grid.get_spin_matrix()))
