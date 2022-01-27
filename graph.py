class node(object):
  def __init__(self,inbound=None, outbound=None):
    self.name = ''


    if inbound:
      self.inbound = inbound
    else:
      self.inbound = []

    if outbound:
      self.outbound = outbound
    else:
      self.outbound = []

  
  def add_outbound_edge(self,node):
    self.outbound.append(node)
    node.inbound.append(self)

  def add_inbound_edge(self,node):
    node.outbound.append(self)
    self.inbound.append(node)
  



class graph(object):
  def __init__(self,nodes = None):
    if nodes:
      self.nodes = nodes
    else:
      self.nodes = {}
      
  def add_node(self,node_name,node):
    node.name = node_name
    self.nodes[node_name] = node

  def add_edge(self,start_node,end_node):
    start = self.nodes[start_node]
    end = self.nodes[end_node]
    start.add_outbound_edge(end)

  def get_neighbours(self,node_name):
    node=self.nodes[node_name]
    neighbours = node.outbound()
    return neighbours

  def remove_node(self,node_name):
    if node_name in self.graph:
      del self.nodes[node_name]
  
  def get_nodes(self):
    nodes = list(self.nodes.values())
    return nodes
