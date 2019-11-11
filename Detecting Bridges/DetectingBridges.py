
import networkx as nx		#importing 'networkx' python package

original_graph = nx.read_gml('lesmis.gml')	#'original_graph' is the name given to the graph that represents the Les Mis network

def bridge_detection(original_graph):
    bridgeSet=[]			#this is a list that stores the bridges in the graph. Created list as it is mutable
    for u,v in original_graph.edges:	#u and v as mentioned in the algorithm are the vertices of the edge
        modified_graph = original_graph.copy()	#'modified_graph' is the copy of the original_graph used as a replication of the original graph with one edge removed every iteration
        modified_graph.remove_edge(u,v)        
        Disconnected = False
        bfs_edges_list = list(nx.bfs_edges(modified_graph,source=u))	#bfs_edges_list stores all the edges obtained on performing the bfs operation
        if not [item for item in bfs_edges_list if v in item]:	#checking if the 'v' vertex is not found in the 'bfs_edges_list' list  
            Disconnected = True
        if Disconnected:			#if Disconnected is True means that vertex v was not found the 'bfs_edges_list' list which indicates that removal of u made it impossible to reach vertex v hence indicating that (u,v) is a bridge
            bridgeSet.append((u,v))	#adding the bridge found in the 'bridgeSet' list used to store all bridges in the graph
    return bridgeSet

def main():
    bridges_in_graph = bridge_detection(original_graph)
    print("\nAll detected bridges in the Les Misérable network are:-\n-------------------------------------------------------")
    for bridges in bridges_in_graph:	#for loop used to print one edge per line as expected 
        print(bridges)
    print('------------------------------------------------------\nTotal',len(bridges_in_graph),'bridges detected in the Les Misérable network\n')


if __name__ == "__main__":	
    main()

