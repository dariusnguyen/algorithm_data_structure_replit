'''
given a list of edges
loop through and find the node without any incoming edge:
	add source to set
	if target in set, remove it
	remaining node is the "root"
from that node, find path by dfs
recursion f()
add node to output list
for each node's neighbor
f(neighbor)

time: 
'''
def edge2adjacency(edges):
	'''
	edges is expected to be a nested list [[v1,v2], [v3,v4]]
	'''
	graph = {}
	for e in edges:
		if e[0] in graph:
			graph[e[0]].append(e[1])
		else:
			graph[e[0]] = [e[1]]
	return graph

def find_root(edges):
	sources = set()
	targets = set()
	for e in edges:
		sources.add(e[0])
		targets.add(e[1])
	return list(sources - targets)[0]

def topological_order(graph, root, path = []):
	path.append(root)
	if root in graph:
		for neighbor in graph[root]:
			topological_order(graph, neighbor, path)
	return path

pairs1 = [
    ["Foundations of Computer Science", "Operating Systems"],
    ["Data Structures", "Algorithms"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"],
]

graph = edge2adjacency(pairs1)
root = find_root(pairs1)
print(graph)
print(root)
order = topological_order(graph, root)
print(order[int(len(order)/2)])