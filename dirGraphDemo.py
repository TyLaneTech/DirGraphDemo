from collections import defaultdict

def graphDrawing():
	print ("                                       ")
	print ("        Directed Graph Example         ")
	print ("                                       ")
	print ("                  0                    ")
	print ("                /   \                  ")
	print ("               3     1                 ")
	print ("              /       \                ")
	print ("             4         2               ")
	print ("              \       / \              ")
	print ("               \     /   8             ")
	print ("                \   /                  ")
	print ("                  5                    ")
	print ("                 /                     ")
	print ("                6                      ")
	print ("               / \                     ")
	print ("              7   9                    ")
	print ("                                       ")
	print ("                                       ")
	print ("                   (Direction is down) ")
	print ("           (Edges are of equal weight) ")
	print ("                                       ")
	print ("                                       ")

def shortestPathContainer():
	
	class DirGraph:	
		def __init__(self,nodes):
			self.N = nodes						#Number of nodes
			self.ogV = nodes 					#Original number of nodes
			self.dirGraph = defaultdict(list)	#Dictionary that Contains graph

		#Creates arc
		def addArc(self,s,t):
			self.dirGraph[s].append(t)			#Adds a key/value pair. key(s) = starting node, value(t) = destination node

		#Prints the shortest path stored in parent[]
		def printPath(self, parent, v):
			pathLength = 1
			if parent[v] == -1 and v < self.ogV:#For first vertex; if v is source, print it
				return 0
			p = self.printPath(parent, parent[v])
			pathLength = p + pathLength			#Increment path length 
			if v < self.ogV:					#Print node if it's less than original node length. (avoids duplicates)
				print (v),
			return pathLength

		#Prints shortest path from src to dest
		def shortestPath(self,src, dest): 
			visited = [False] * (self.N) 		#Holds indication of whether or not a node has been visited
			parent = [-1] * (self.N)	 		#Contains the parent of the current node
			queue = [] 							#Create a queue for BFS 

			queue.append(src) 					#Adds vertex to queue
			visited[src] = True 				#Marks vertex as visited

			while queue : 
				s = queue.pop(0) 				#Pop the top vertext 
				if s == dest: 					#If s = dest print the path & return
					return self.printPath(parent, s) 
					
				for i in self.dirGraph[s]: 		#Get adjacent nodes of s (last vertex popped from queue) 
					try:
						if visited[i] == False: #If an adjacent vertex has'nt been visited...
							queue.append(i) 	#Enqueue it
							visited[i] = True 	#Mark it visited
							parent[i] = s 		#Set the parent to the current vertex, and move on
					except IndexError:
						print ("not possible.")
						pass

	dg = DirGraph(10)							#Create graph with 10 nodes
	dg.addArc(0, 1)								#Add arc (edge) from node 0 to 1
	dg.addArc(0, 3)								#Add arc (edge) from node 0 to 3
	dg.addArc(1, 2)								#Add arc (edge) from node 1 to 2
	dg.addArc(2, 5)								#Add arc (edge) from node 2 to 5
	dg.addArc(3, 4)								#Add arc (edge) from node 3 to 4
	dg.addArc(4, 5)								#Add arc (edge) from node 4 to 5
	dg.addArc(5, 6)								#Add arc (edge) from node 5 to 6
	dg.addArc(6, 7)								#Add arc (edge) from node 6 to 7
	dg.addArc(2, 8)								#Add arc (edge) from node 2 to 8
	dg.addArc(6, 9)								#Add arc (edge) from node 6 to 9

	print ("")
	print ("")
	print ("Shortest path from %d to %d is: " %(src, dest))
	try:
		l = dg.shortestPath(src, dest)			#Calls shoortestPath() function
		print ("Shortest distance between %d and %d is: %d " %(src, dest, l)),
	except:
		print("not possible.")

		
graphDrawing()									#Calls function to print graph	
src = int(input("Enter starting node: "))		#Input for source node
dest = int(input("Enter destination node: "))	#Input for destination node
shortestPathContainer()									
