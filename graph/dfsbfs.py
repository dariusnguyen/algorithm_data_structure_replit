
def dftraverse(graph, source):
	#iterative
	# stack = [source]
	# while len(queue)>0:
	# 	curr = stack.pop()
	# 	print(curr)
	# 	for neighbor in graph[curr]:
	# 		stack.append(neighbor)
	
	#recursive
	print(source)
	for neighbor in graph[source]:
		dftraverse(graph, neighbor)

def bftraverse(graph, source):
	#only iterative solution is possible
	q = [source]
	while len(q)>0:
		curr = q.pop()
		print(curr)

		for neighbor in graph[curr]:
			q.insert(0, neighbor)

def haspath_dfs(graph, src, dest): #check if a path from src to dest exists
	#iterative
	# stack = [src]
		
	# while len(stack)>0:
	# 	curr = stack.pop()
	# 	if curr == dest:
	# 		return True
	# 	for neighbor in graph[curr]:
	# 		stack.append(neighbor)

	# return False
	
	#recursive
	if src == dest:
		return True

	for neighbor in graph[src]:
		if haspath_dfs(graph, neighbor, dest):
			return True
			
	return False

def haspath_bfs(graph, src, dest):
	q = [src]
	while len(q)>0:
		curr = q.pop()
		if curr == dest:
			return True
		for neighbor in graph[curr]:
			q.insert(0, neighbor)
	return False
				
def edges2adjacency(edges):
	graph = {}
	#assumming undirected graph
	for edge in edges:
		n1 = edge[0]
		n2 = edge[1]
		if graph.get(n1) is None:
			graph[n1] = [n2]
		else:
			graph[n1].append(n2)
			
		if graph.get(n2) is None:
			graph[n2] = [n1]
		else:
			graph[n2].append(n1)
	return graph

def haspath_dfs(graph, src, dest, visited):
	'''
	new version that uses a "visited" set to avoid cycles (infinite loops) in cyclic graphs
	'''
	
	if src == dest:
		return True
	if src in visited:
		return False
	visited.add(src)
		
	for neighbor in graph[src]:
		if haspath_dfs(graph, neighbor, dest, visited):
			return True
		
	return False

def count_connected_components(graph):
	'''
	algorithm to count connected components:
	- create a visit_dfs() recursive function to traverse the graph given a source node, and add visited node to the set
	- loop through list of nodes in the graph
		if the node is in the visited set, skip it
		if the node is not visited
			use visit_dfs() to visit the nodes
			increment components count
	- return final components count
	'''
	def visit_dfs(graph, src, visited):
		if src not in visited:
			visited.add(src)
			for neighbor in graph[src]:
				visit_dfs(graph, neighbor, visited)
	
	visited = set()
	count = 0
	for node in graph.keys():
		if node not in visited:
			visit_dfs(graph, node, visited)
			count += 1
	return count

edges = [['a', 'c'],
		 ['a', 'b'],
		 ['b', 'd'],
		 ['c', 'e'],
		 ['d', 'f']]

graph = {
	'a': ['c', 'b'],
	'b': ['d'],
	'c': ['e'],
	'd': ['f'],
	'e': [],
	'f': []
}
