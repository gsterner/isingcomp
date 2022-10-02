import polymersim as poly
import system_translation as systrans
import connection_matrix_creation as cmc
import polymerstatistics as polstat

#Randomize polymer
polymer_positions = poly.random_walk(10)
print(polymer_positions)
#Check for clashes
has_duplicate = polstat.has_duplicates(polymer_positions)
print(has_duplicate)

#if there is a clash
#translate to spins
spin_system = systrans.translate_positions_to_spins(polymer_positions)
print(spin_system)
#make J-matrix
connections = cmc.outer_square(spin_system)
print(connections)

#Add to total J-matrix
