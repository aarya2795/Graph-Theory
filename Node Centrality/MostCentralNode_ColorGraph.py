#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from numpy import linalg as LA
from collections import defaultdict


# In[2]:


Knetwork = nx.krackhardt_kite_graph()


# In[4]:


nx.draw(Knetwork, with_labels = True)


# <ol type = "I">
#    <li> Degree Centrality - The most central node for this measure for krackhardt_kite_graph is <b>node 3</b> as it has maximum degree(6) among the degrees of all other nodes. In the network plotted at the bottom this node is shown using <b>green color</b>.</li>
#     <li> Closeness Centrality - The most central node for this measure for krackhardt_kite_graph is the one with the highest centrality measure value. Reason for this is that as the more central a node is, the closer it is to all other nodes. In the Krackhardt_kite network, <b>nodes 5 and 6</b> are the most central nodes for the closeness centrality measure. In the network plotted at the bottom these nodes are shown using <b>violet color</b>.</li>
#     <li> Eigenvector Centrality - The most central node for this measure for krackhardt_kite_graph is the one with the highest eigenvector centrality value. Reason for this is that a high value of eigenvector centrality indicates that the node is connected to many nodes who themselves have high scores. In the Krackhardt_kite network, <b>node 3</b> is the most central node for the Eigen Vector Centrality measure. In the network plotted at the bottom this node is shown using <b>green color</b>.</li>
#     <li> Betweennes Centrality Measure - The most central node for this measure for krackhardt_kite_graph is the one with the highest betweenness centrality value. Reason for this is that a higher betweenness centrality value of the node means that the node is more influential compared to the rest of the nodes in the network. This means they are of higher importance and message passing between them is crucial. It also would imply that the removal of this node would cause problems in communication as they appear on most of the paths between the nodes. In the Krackhardt_kite network, <b>node 7</b> is the most central node for the betweenness centrality measure. In the network plotted at the bottom this node is shown using <b>blue color</b>.</li>
# <ol>

# In[5]:


color_map = ['yellow', 'yellow', 'yellow',  'green', 'yellow', 'violet', 'violet', 'blue', 'yellow', 'yellow']
nx.draw(Knetwork, with_labels = True, node_color = color_map)
plt.show()

