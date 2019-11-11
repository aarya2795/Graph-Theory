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


# In[3]:


nx.draw(Knetwork, with_labels = True)


# In[4]:


norm_degree_centrality = []              #stores the normalized degree centrality vector
number_of_nodes = Knetwork.number_of_nodes()
for i,j in list(Knetwork.degree()):
    norm_degree_centrality.append((j / (number_of_nodes-1)))


# In[5]:


print("Vector of normalized degree centralities:- ")
norm_degree_centrality

