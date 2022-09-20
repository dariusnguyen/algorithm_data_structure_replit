def arrays_test():
	from arrays_strings import scheduleMeeting as s
	input1 = [ [[60,150], [180,240]],
			  [[0,210], [360,420]] ]
	input2 = 121
	# solution (schedules, length) = 240
	res = s.solution(input1, input2)
	print(res)
	# print(input1[res[0]], input1[res[1]])

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
	from trees.tree_base import Node
	
	# from trees import rightsideview as rsv
	
	# input1 = rsv.Node(1, rsv.Node(2, None, rsv.Node(5, rsv.Node(6), None)), rsv.Node(3, None, rsv.Node(4)))
	# print(rsv.rightsideview(input1))

	'''
 	# Binary Search Trees
	from trees import validate_BST
	input1 = Node(5, Node(1), Node(8, Node(6), Node(9)))
	input2 = Node(5, Node(1), Node(4, Node(3), Node(6)))
	input3 = Node(2, Node(2), Node(2))
	print('test case 1:', validate_BST.isValidBST_3(input1))
	print('test case 2:', validate_BST.isValidBST_3(input2))
	print('test case 3:', validate_BST.isValidBST_3(input3))
	'''

	
	# Binary Trees:
	from trees import M_sumRootToLeafNumbers as srtl
	"""
 					1
	  	2						3
      4   5                   6
 	"""
	input1 = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), None) )
	print(srtl.sumRootToLeafNumbers(input1))
	

	'''
	#array to BST
	from trees import sortedArray2BST
	from trees import binaryTreeTraversals

	input1 = [-10,-3,0,5,9]

	mytree = sortedArray2BST.sortedArray2BST(input1)
	print(binaryTreeTraversals.preorder(mytree))
 	'''
	

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
	# from dp import M_mimimumCoinChange as mcc
	from backtracking import M_combinationSum as cs
	# input1 = [2]
	input1 = [2,3,6,7]
	input2 = 7
	# print(can_sum.best_sum_dp(input1, input2))

	# input1 = 'wwwwwwwwwwwwwwwwwwwwwwwww'
	# input2 = ['w', 'ww','www', 'wwwww', 'wwww']
	# input1 = 'abcdef'
	# input2 = ['a', 'abc','dex', 'def', 'cdef', 'bc']

	# input1 = 'target'
	# input2 = ['t', 'a', 'abc','r', 'gef', 'get', 'ge', 'tar', 'e']

	# input1 = 'purple'
	# input2 = ['purp', 'p', 'ur', 'le', 'purpl']
	
	print(cs.combinationSum(input1, input2))


def linked_list_test():
	# from linked_list import linked_list_base as llb
	from linked_list.linked_list_base import Node
	from linked_list import reverseGroupsOfK
	
	# Node5 = Node(5, None)
	# Node4 = Node(4, Node5)
	
	# input1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	# input2 = Node(5, Node(5, Node(5, None)))
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	n4 = Node(4)
	n5 = Node(5)
	n6 = Node(6)
	n7 = Node(7)
	n8 = Node(8)
	
	n1.next = n2
	# n2.prev = n1
	n2.next = n3
	# n3.prev = n2
	n3.next = n4
	# n4.prev = n3
	# n4.next = n5
	# n5.prev = n4
	# n5.next = n6
	# n6.prev = n5
	# n6.next = n7
	# n7.prev = n6
	# n7.next = n8
	# n8.prev = n7

	input1 = n1
	
	input1.print_list()
	
	res = reverseGroupsOfK.reverse(input1, 3)
	res.print_list()

	

print('Test result:')
# linked_list_test()
# arrays_test()
dp_test()
# trees_test()