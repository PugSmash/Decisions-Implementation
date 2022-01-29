from graph import graph, node, edge

one = node()
two = node()
three = node()
four = node()
five = node()
six = node()
A = edge("1", "2", 6, "A")
B = edge("1", "3", 6, "B")
C = edge("3", "4", 6, "C")
D = edge("2", "4", 6, "D")
E = edge("4", "5", 6, "E")
F = edge("5", "6", 6, "F")


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

for i in graph.get_neighbours("1"):
    print(i.name)
