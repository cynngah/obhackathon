edges_file = open("edges_world_1.clq")
nodes_file = open("nodes_world_1.txt")
adj_list = {}
node_list = []
max_clique = [] 

class Node:

  def __init__(self, number):
    self.number = number
    self.color = "white"

for line in nodes_file: 
  node_info = line.split() # node[0] is node number, node[1] is role (Issuer/Dealer/Investor)
  node = Node(int(node_info[0]))
  adj_list[node] = []
  node_list.append(node)

for line in edges_file:
  edge = line.split() #edge[0] is useless crap, edge[1] is source, edge[2] is destination, edge[3] is comm. method
  source_node_number = int(edge[1]) 
  dest_node_number = int(edge[2])
  adj_list[node_list(source_node_number - 1)].append(node_list[dest_node_number - 1])

"""
@param graph: Adjacency list representing the graph
"""
def 

"""
@param graph: adjacency list representing graph
@return true if graph is a clique 
"""
def is_clique(graph):

# check if adjacency list for all nodes is same length
