import numpy as np
import networkx as nx
from google.colab import output # It was used only to clean the output.

class DIJKSTRA():
  
  def __init__(self,num_node,labels):
    """
    Number of node (num_node) must be equal to number of labels.

    Number of node (num_node) is integer
    Labels (labels) is array 1xn
  
    """
    self.num_node=num_node
    self.labels=labels
    self.ways=[]

  def automatic_create_graph(self,val_range):
    """
    You can create to graph automatically.

    Value of range (val_range) is array 1x2
    """
    self.distances=np.zeros((self.num_node,self.num_node),dtype="int32")# Create an empty array according to the number of node.
  
    # Fill the empty array with random numbers.
    for i in range(self.num_node):
      distancesX=np.random.randint(val_range[0],val_range[1],(1,self.num_node-1))
      distancesX=np.insert(distancesX,[i],0)
      distancesY=distancesX.reshape(self.num_node,1)
      self.distances[i]=distancesX

      for j in range(self.distances.shape[0]):
        self.distances[j][i]=distancesY[j][0]
    
    return self.distances

  def manuel_create_graph(self):
    """
    You can create to graph manuel.

    Distances must be real number.
    """
    self.distances=np.zeros((self.num_node,self.num_node),dtype="int32")# Create an empty array according to the number of node.

    # Fill the empty array with entered numbers.
    i=0
    while i!=self.num_node:
      j=0
      while j!=self.num_node:
        if i!=j and j>i:
          try:
            self.distances[i][j]=float(input(f"Write the distance between {self.labels[i]} and {self.labels[j]}: "))
          except:
            print("Please enter a number")
            j-=1

        j+=1
      i+=1
    output.clear()# It's here.
                  
    for i in range(self.num_node):
      distancesY=self.distances[i].reshape(self.num_node,1)
      for j in range(self.num_node):
        self.distances[j][i]=distancesY[j][0]

    return self.distances     

  def create_tuple(self):
    """
    Create a tuple for the calculate.
    """
    for i in range(self.num_node):
      for j in range(self.num_node):
        self.ways.append((self.labels[i],self.labels[j],self.distances[i][j]))
    return self.ways
  
  def calculate_route(self,start_point,finish_point):
    """
    Calculate the best route.
    """
    G=nx.Graph()
    total_way=0
    x=""

    G.add_weighted_edges_from(self.ways)
    route=nx.dijkstra_path(G,start_point,finish_point)# Calculate the best route with networkx.

    # Create the result.
    for i in range(len(route)-1):
      for j in self.ways:
        if (j[0] == route[i]) and (j[1] == route[i+1]):
          total_way+=j[2]
          x+=f"{route[i]} -> ({j[2]}) "

    return f"{x+route[-1]} : {total_way}"
