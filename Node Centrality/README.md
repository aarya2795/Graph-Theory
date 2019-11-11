<h1>Finding Most Central Node</h1>
<br>Write a self-contained and fully functional Jupyter Notebook that:
 
<ol type="1">
<li>Loads the necessary libraries to run (e.g., NetworkX, Matplotlib) </li>
<li>Loads Krackhardt’s network of friendship among high-tech managers (see below) </li>
<li>Computes the adjacency matrix A </li>
<li>Computes, for all nodes: </li>
<ol type="a">
<li>The vector of normalized degree centralities</li>
<li>The vector of closeness centralities</li>
<li>The vector of eigenvector centralities</li>
<li>The vector of betweenness centralities</li>
</ol>
</ol>

Plot the network using NetworkX’s draw function and use colors to highlight any difference between the various centrality measures.
What is the most central node for each measure

<h2> Definition of each centrality measure, and description of how it is computed </h2>

<ol type = "I">
<li><h3><u>Normalized Degree Centrality</u> :-</h3>
    <br>First we define "degree centrality" measure and then the "normalized degree centrality" measure
    <br><br><b>Degree Centrality</b> - Simple centrality measure which counts the number of neighbors a node has.
    The degree centrality Cd for node vi in
an undirected graph is
Cd(vi) = di; (3.1)
where di is the degree (number of adjacent edges) of node vi.
    <br><br><b>Normalized Degree Centrality</b> - To overcome the problem of degree centralities not allowed to be compared between different networks, we need to normalize the degree centrality values.
    <br> Simple normalization is done by dividing the degree centrality by the maximum possible degree; this yields measures ranging from 0 to 1. This is computed as follows:-<br><b>$$C^{norm}_{d}(v_i) =\frac{d_i}{n-1} ,$$</b>
    <br> &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;where n is the number of nodes.
    <br>
    <br><br><b>Most Central Node</b>
    <b> 
    <br> Reason:</b> Degree centrality assumes that the node with the maximum degree is the
most central individual.<br>The most central node for the degree centrality measure for krackhardt_kite_graph is <b>node 3</b> as it has maximum degree(6) among the degrees of all other nodes. In the network plotted at the bottom this node is shown using <b>green color</b>.
</li>
<li>
<h3><u> Closeness Centrality Measure </u></h3>
<br><b> Definition: </b>Closeness centrality is defined as: A measure to calculate the closeness of a node in the network. <br>It is computed as: <br> $$C_c(v_i) = \frac{1}{\bar{l}_{v_i}} ,  $$<br> &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;where ${\bar{l}_{v_i}} = \frac{1}{n-1}\displaystyle{ \sum_{v_i ≠ v_j}}l_{i,j}$ is node v<sub>i</sub>’s average shortest path length to other
nodes. 
<br><br><b>Most Central Node</b><br>The most centralnode for this measure is the one with the highest centrality measure value.<br><b>Reason</b> As the more central a node is, the closer it is to all other nodes.<br>E.g. in the Krackhardt_kite network, <b>nodes 5 and 6</b> are the most central nodes for the closeness centrality measure. In the network plotted at the bottom these nodes are shown using <b>violet color</b>.
</li>
<li>
<h3><u>Eigenvector Centrality Measure</u></h3>
<br><b> Definition: </b> It is basically a measure of influence of a node in a network. This measure considers the importance of its neighbors and tries to generalize the degree centrality measure
<br> $$c_e(v_i) = \frac{1}{\lambda} \sum^n_{j=1} A_{j,i} \,c_e(v_j) , $$<br> where λ is some fixed constant. Assuming C<sub>e</sub> = (C<sub>e</sub>(v<sub>1</sub>), C<sub>e</sub>(v<sub>2</sub>), . . . , C<sub>e</sub>(v<sub>n</sub> ))<sup>T</sup>
is the centrality vectors for all nodes, we can rewrite the above equation as &emsp;&emsp;λC<sub>e</sub> = A<sup>T</sup>C<sub>e</sub> .. this means that C<sub>e</sub> is an eigenvector of adjacency matrix A<sup>T</sup> and λ is the corresponding eigenvalue.<br> On obtaining the eigen values we select the largest eigen value and then using this we compute the corresspodning eigenvector.
<br><br><b>Most Central Node</b><br>The node with the highest eigenvector centrality value is the most central node<br><b>Reason:</b> as a high value of eigenvector centrality indicates that the node is connected to many nodes who themselves have high scores><br>E.g. in the Krackhardt_kite network, node 3 is the most central node for the Eigen Vector Centrality measure. In the network plotted at the bottom this node is shown using <b>green color</b>.
</li>
<li>
<h3><u>Betweennes Centrality Measure</u></h3>
<br><b> Definition: </b> It is basically a measure of influence of node among a network on the other nodes of the network. It measures how much a vertex lies on the paths between other vertices. <br>It is computes using the following equation: <br>$$\displaystyle{C_b(v_i) = \sum_{s!=t!=v_i}  \frac{σ_{st}(v_i)}{σ_{s,t}}}$$ <br> σ<sub>st</sub> is the number of shortest paths from node s to t (also known
as information pathways), and σ<sub>st</sub>(v<sub>i</sub>) is the number of shortest paths from s
to t that pass through v<sub>i</sub><br><br><b>Most Central Node</b> The most central node for this measure is the one with the highest betweenness centrality value.<br><b>Reason:</b>A higher betweenness centrality value of the node means that the node is more influential compared to the rest of the nodes in the network. This means they are of higher importance and message passing between them is crucial. It also would imply that the removal of this node would cause problems in communication as they appear on most of the paths between the nodes.<br><br>E.g. in the Krackhardt_kite network, <b>node 7 is the most central node</b> for the betweenness centrality measure. In the network plotted at the bottom this node is shown using <b>blue color</b>.
</li>
</ol>


