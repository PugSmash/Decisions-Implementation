class node(object):
    def __init__(self, inbound=None, outbound=None):
        self.name = ''

        if inbound:
            self.inbound = inbound
        else:
            self.inbound = []

        if outbound:
            self.outbound = outbound
        else:
            self.outbound = []

    def add_outbound_edge(self, node):
        self.outbound.append(node)
        node.inbound.append(self)

    def add_inbound_edge(self, node):
        node.outbound.append(self)
        self.inbound.append(node)


class graph(object):
    def __init__(self, nodes=None):
        if nodes:
            self.nodes = nodes
        else:
            self.nodes = {}
        self.edges = []

    def add_node(self, node_name, node):
        node.name = node_name
        self.nodes[node_name] = node

    def add_edge(self, edge):
        start = self.nodes[edge.start_node]
        end = self.nodes[edge.end_node]
        start.add_outbound_edge(end)
        self.edges.append(edge)

    def get_neighbours(self, node_name):
        node = self.nodes[node_name]
        return node.outbound

    def remove_node(self, node_name):
        if node_name in self.graph:
            del self.nodes[node_name]

    def get_nodes(self):
        nodes = list(self.nodes.values())
        return nodes

    def get_edge(self, start, end):
        for edge in self.edges:
            if edge.start_node == start and edge.end_node == end:
                return edge
            else:
                pass


class edge:
    def __init__(self, start_node, end_node, weight, name):
        self.start_node = start_node
        self.end_node = end_node
        self.weight = weight
        self.name = name
