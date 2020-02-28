class Vertex:

    def __init__(self, spin_value, neighbours, coordinate):
        self.spin_value = spin_value
        self.neighbours = neighbours
        self.row = coordinate[0]
        self.column = coordinate[1]

    def flip_spin(self):
        self.spin_value = -self.spin_value

    def hamiltonian(self):
        return 0.1

    def pp(self):
        print('spin_value: ' + str(self.spin_value))
        print('row: ' + str(self.row) + ' column: ' + str(self.column))
