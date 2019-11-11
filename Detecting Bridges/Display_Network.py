import networkx as nx

import matplotlib.pyplot as plt

network = nx.read_gml('lesmis.gml')

nx.draw(network)

plt.show()

