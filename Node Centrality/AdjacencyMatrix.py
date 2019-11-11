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


#Adjacency matrix for the krackhardt_kite network
Adjacency_matrix = [ [0] * Knetwork.number_of_nodes() for i in range(Knetwork.number_of_nodes())]
for row, column in list(Knetwork.edges):
    Adjacency_matrix[row][column] = 1              #edge exists between i and j so insert 1
    Adjacency_matrix[column][row] = 1              #value of A[j][i] equals A[i][j] since krackhardt_kite is an undirected graph


# In[6]:


print("Adjacency Matrix for the krackhardt_kite network:- ")
Adjacency_matrix

