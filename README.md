I. OVERVIEW

A directed graph is a graph where the arcs have a direction associated with them. This direction in the nodes can represent asymmetrical relationships between nodes. Directed graphs can be used to model road networks, deterministic finite automation, or even predator prey relationships. This document demonstrates a basic way to implement a directed graph in Python, and includes a demo to further illustrate the data structure.



II. HOW DOES IT WORK?

Implementing this data structure in Python is pretty straight forward. Using a dictionary, items can be stored in a key value pair. The 'key' represents the 'source-node' and the 'value' represents the 'target-node'; this 'source-target' relationship is how we establish the direction of the arcs between nodes. Creating directed graph in Python can be accomplished like this:

#first create a method to initialize the dictionary, and gets the number of nodes:
class DirGraph:
	def __init__(self,nodes):
		self.N = nodes				            #Number of nodes	
		self.dirGraph = defaultdict(list)	#Dictionary containing graph

#then create a method to add the arc to the dictionary (dirGraph):
	def addArc(self,s,t):                   #'s' & 't' represent the source, and target nodes of an arc.
		self.dirGraph[s].append(t)	    	#Add arc to dictionary

#then construct the graph:
	dg = DirGraph(10)		#Initialize graph with 10 nodes
	dg.addArc(0, 1)			#Add arc (edge) from node 0 to 1
	dg.addArc(0, 3)			#Add arc (edge) from node 0 to 3
	dg.addArc(1, 2)			#Add arc (edge) from node 1 to 2
	dg.addArc(2, 5)			#Add arc (edge) from node 2 to 5
	dg.addArc(3, 4)			#Add arc (edge) from node 3 to 4
	dg.addArc(4, 5)			#Add arc (edge) from node 4 to 5
	dg.addArc(5, 6)			#Add arc (edge) from node 5 to 6
	dg.addArc(6, 7)			#Add arc (edge) from node 6 to 7
	dg.addArc(2, 8)			#Add arc (edge) from node 2 to 8
	dg.addArc(6, 9)			#Add arc (edge) from node 6 to 9
#End of code


This will create a directed graph that resembles the following:
	                                         
	                   0                     
	                 /   \                   
	                3     1                  
	               /       \                 
	              4         2                
	               \       / \               
	                \     /   8              
	                 \   /                   
	                   5                     
	                  /                      
	                 6                       
	                / \                      
	               7   9                     

NOTE: Direction of the arcs in this illustration is downward (ie. 0 to 3 is possible but 3 to 0 is not). This 'Downward' direction of the arcs is totally relative to the graphs orientation, and isn't always the case. Refer to dirGraph.png for a more applicable illustration.



III. HOW IS THIS DATA STRUCTURE USEFUL?

Directed graphs are used to model asymmetric relationships between nodes (ie. direction). Unlike an undirected graph where all nodes have symmetrical relationships.

Directed graphs can be used to model:
Road Networks (using the arc's direction to represent a streets direction)
Predator-Prey Relationships
Financial Trade, etc.

Many real world scenarios involving an ordered relationship can use directed graphs to model their characteristics.



IV. FURTHER READING

https://cs.stackexchange.com/questions/68163/why-are-directed-graphs-important
https://www.bogotobogo.com/python/python_graph_data_structures.php
https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
