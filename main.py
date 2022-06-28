def arrays_test():
	from arrays_strings import subdomain_visit_count as svc
	input1 = ["9001 discuss.leetcode.com"]
	
	print(svc.count_domain_visits(input1))

def graph_test():
	from graph import dfsbfs
	input1 = {
		'a': ['c', 'b'],
		'b': ['d'],
		'c': ['e'],
		'd': ['f'],
		'e': [],
		'f': []
	}
	input1 = {
		'f': ['g', 'i'],
		'g': ['h'],
		'h': [],
		'i': ['g', 'k'],
		'j': ['i'],
		'k': []
	}
	
	input1 =[['a', 'c'],
			 ['a', 'b'],
			 ['b', 'd'],
			 ['c', 'e'],
			 ['d', 'f'],
			 ['b', 'c'],
			 ['i', 'j']]
	
	input2 = 'e'
	input3 = 'j'
	graph = dfsbfs.edges2adjacency(input1)
	input4 = set()
	# print(dfsbfs.haspath_dfs(graph, input2, input3, input4))
	print(dfsbfs.count_connected_components(graph))

def trees_test():
	from trees import rightsideview as rsv
	
	input1 = rsv.Node(1, rsv.Node(2, None, rsv.Node(5, rsv.Node(6), None)), rsv.Node(3, None, rsv.Node(4)))
	print(rsv.rightsideview(input1))

def binary_search_test():
	from binary_search import search2d
	# input1 =[[1,3,5,7],
	# 		 [10,11,16,20],
	# 		 [23,30,34,60]]
	
	input1 =[[3,3,3,3],
			 [10,10,10,10],
			 [23,30,34,60]]
	
	input2 = 10
	
	print(search2d.binary_search_2d(input1, input2))


def dp_test():
	from dp import strings
	# input1 = 300
	# input2 = [7,40]
	# input1 = 10
	# input2 = [1,2,5]
	# input1 = 8
	# input2 = [2,3,5]
	# print(can_sum.best_sum_dp(input1, input2))

	input1 = 'wwwwwwwwwwwwwwwwwwwwwwwww'
	input2 = ['w', 'ww','www', 'wwwww', 'wwww']
	# input1 = 'abcdef'
	# input2 = ['a', 'abc','dex', 'def', 'cdef']
	print(strings.count_construct_dp(input1, input2))


def linked_list_test():
	# from linked_list import linked_list_base as llb
	from linked_list.linked_list_base import Node
	from linked_list import swapNodesInPairs
	
	# Node5 = Node(5, None)
	# Node4 = Node(4, Node5)
	
	input1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	# input2 = Node(5, Node(5, Node(5, None)))
	
	input1.print_list()
	# input2.print_list()

	res = swapNodesInPairs.swap_pairs_recur(input1)
	res.print_list()



linked_list_test()