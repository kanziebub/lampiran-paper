# Python3 program for Bellman-Ford's single source
# shortest path algorithm.

# Class to represent a graph
class Graph:

 def __init__(self, vertices):
  self.V = vertices # No. of vertices
  self.graph = []
  self.hospitals = []
  self.nearestHospitals = []

 # function to add an edge to graph
 def addEdge(self, u, v, w):
  self.graph.append([u, v, w])
 
 def addHospital(self, v):
  self.hospitals.append(v)

 # utility function used to print the solution
 def findHospital(self, dist):
  for i in range(self.V):
   if i in self.hospitals:
    self.nearestHospitals.append([i+1, dist[i]])

 def printHosp(self):
  min = self.nearestHospitals[0]
  for i in range(0, len(self.nearestHospitals)):  
   if(self.nearestHospitals[i][1] < min[1]):    
    min = self.nearestHospitals[i]; 
  print("Nearest hospital is vertex ", min[0], " with a cost of ", min[1])
    
 
 # The main function that finds shortest distances from src to
 # all other vertices using Bellman-Ford algorithm. The function
 # also detects negative weight cycle
 def BellmanFord(self, src):

  # Step 1: Initialize distances from src to all other vertices
  # as INFINITE
  dist = [float("Inf")] * self.V
  dist[src] = 0


  # Step 2: Relax all edges |V| - 1 times. A simple shortest
  # path from src to any other vertex can have at-most |V| - 1
  # edges
  for _ in range(self.V - 1):
   # Update dist value and parent index of the adjacent vertices of
   # the picked vertex. Consider only those vertices which are still in
   # queue
   for u, v, w in self.graph:
    new = dist[u] + w
    if dist[u] != float("Inf") and new < dist[v]:
      dist[v] = new

  # Step 3: check for negative-weight cycles. The above step
  # guarantees shortest distances if graph doesn't contain
  # negative weight cycle. If we get a shorter path, then there
  # is a cycle.

  for u, v, w in self.graph:
    if dist[u] != float("Inf") and dist[u] + w < dist[v]:
      print("Graph contains negative weight cycle")
      return
      
  # print all distance
  self.findHospital(dist)
  self.printHosp()

g = Graph(32)

g.addHospital(0)
g.addHospital(4)
g.addHospital(9)
g.addHospital(10)
g.addHospital(14)
g.addHospital(15)
g.addHospital(27)

g.addEdge(0, 1, 65)
g.addEdge(1, 2, 400)
g.addEdge(2, 3, 60)
g.addEdge(3, 4, 750)
g.addEdge(4, 5, 550)
g.addEdge(5, 6, 300)
g.addEdge(6, 7, 650)

g.addEdge(7, 8, 170)
g.addEdge(8, 9, 180)
g.addEdge(8, 10, 350)
g.addEdge(10, 11, 600)
g.addEdge(11, 12, 1100)
g.addEdge(12, 13, 300)
g.addEdge(13, 14, 250)

g.addEdge(13, 15, 290)
g.addEdge(15, 16, 280)
g.addEdge(16, 17, 600)
g.addEdge(17, 18, 270)
g.addEdge(18, 6, 550)
g.addEdge(17, 19, 1400)
g.addEdge(19, 20, 100)

g.addEdge(19, 21, 220)
g.addEdge(21, 22, 170)
g.addEdge(22, 1, 650)
g.addEdge(16, 23, 72)
g.addEdge(23, 24, 250)
g.addEdge(23, 31, 1700)
g.addEdge(24, 25,3300)

g.addEdge(25, 30, 190)
g.addEdge(30, 31, 140)
g.addEdge(25, 26, 250)
g.addEdge(29, 31, 260)
g.addEdge(28, 29, 140)
g.addEdge(27, 28, 150)
g.addEdge(26, 28,27)
# ==================== reverse
g.addEdge(1, 0, 65)
g.addEdge(2, 1, 400)
g.addEdge(3, 2, 60)
g.addEdge(4, 3, 750)
g.addEdge(5, 4, 550)
g.addEdge(6, 5, 300)
g.addEdge(7, 6, 650)

g.addEdge(8, 7, 170)
g.addEdge(9, 8, 180)
g.addEdge(10, 8, 350)
g.addEdge(11, 10, 600)
g.addEdge(12, 11, 1100)
g.addEdge(13, 12, 300)
g.addEdge(14, 13, 250)

g.addEdge(15, 13, 290)
g.addEdge(16, 15, 280)
g.addEdge(17, 16, 600)
g.addEdge(18, 17, 270)
g.addEdge(6, 18, 550)
g.addEdge(19, 17, 1400)
g.addEdge(20, 19, 100)

g.addEdge(21, 19, 220)
g.addEdge(22, 21, 170)
g.addEdge(1, 22, 650)
g.addEdge(23, 16, 72)
g.addEdge(24, 23, 250)
g.addEdge(31, 23, 1700)
g.addEdge(25, 24,3300)

g.addEdge(30, 25, 190)
g.addEdge(31, 30, 140)
g.addEdge(26, 25, 250)
g.addEdge(31, 29, 260)
g.addEdge(29, 28, 140)
g.addEdge(28, 27, 150)
g.addEdge(28, 26, 27)

g.addEdge(11, 31, 1200)


# Print the solution
g.BellmanFord(20)

# note that in this code version,
# the vertex starts from 0 instead of 1
# the output was adjusted in line 24

# Initially, Contributed by Neelam Yadav
# Later On, Edited by Himanshu Garg
# https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/
# Adjusted by Nabila Khansa 1906293221 to fit paper