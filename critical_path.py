import random
from unicodedata import name
from graph import graph, node, edge


one = node(source_node=True)
two = node()
three = node()
four = node()
five = node()
six = node(sink_node=True)
A = edge("1", "2", 6, "A")
B = edge("1", "3", 4, "B")
C = edge("3", "4", 2, "C")
D = edge("2", "4", 7, "D")
E = edge("4", "5", 1, "E")
F = edge("5", "6", 9, "F")


graph = graph()

graph.add_node("1", one)
graph.add_node("2", two)
graph.add_node("3", three)
graph.add_node("4", four)
graph.add_node("5", five)
graph.add_node("6", six)
graph.add_edge(A)
graph.add_edge(B)
graph.add_edge(C)
graph.add_edge(D)
graph.add_edge(E)
graph.add_edge(F)

for key in graph.nodes:
    if graph.nodes[key].source_node:
        source = graph.nodes[key]

current_node = source
route = []


def traverse(start_node):
    route_taken = start_node.outbound[random.randint(0, (len(start_node.outbound) - 1))]
    return route_taken

def check_edge(start_node, end_node):
    for edge in graph.edges:
        if edge.start_node == start_node and edge.end_node == end_node:
            print(edge.name)
            return int(edge.weight)
        else:
            pass

while current_node.name != "6":
    route.append(current_node.name)
    current_node = traverse(current_node)

route.append("6")

print(route)

weight_of_route = 0

for i in range(len(route) - 1):
    start_node = route[i]
    end_node = route[i+1]
    weight_of_route += check_edge(start_node, end_node)
    
    

print("Weight of Route: ", weight_of_route)