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


# In[5]:


closeness_centrality_vector = []
for vertex in Knetwork.nodes():
    sum_of_values = 0
    short_list_Knet = nx.shortest_path_length(Knetwork, vertex)
    short_list_Knet.pop(vertex)
    for value in short_list_Knet.values():
        sum_of_values = sum_of_values + value
    sum_of_shortest_path_length = sum_of_values
    number_of_remaining_nodes = len(short_list_Knet.keys())
    avg_shortest_path_length = sum_of_shortest_path_length / number_of_remaining_nodes
    closeness_centrality_vector.append(1 / avg_shortest_path_length)


# In[6]:


print("The vector of closeness centralities:- ")
closeness_centrality_vector


# In[ ]:




