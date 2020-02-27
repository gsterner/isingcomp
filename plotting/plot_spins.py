import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import argparse
import sys
sys.path.append('../src')
import systemdata

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

system_data = systemdata.SystemData(args.filename)
spin_matrix = system_data.spins

fig, ax = plt.subplots()
i = ax.imshow(spin_matrix, cmap=cm.Greys, interpolation='nearest')
plt.show()
