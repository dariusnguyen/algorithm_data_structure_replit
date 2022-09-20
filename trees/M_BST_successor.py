'''
285. Inorder Successor in BST
Medium

Given the root of a binary search tree and a node p in it, return the in-order successor of that node in the BST. If the given node has no in-order successor in the tree, return null.

The successor of a node p is the node with the smallest key greater than p.val.

Example 1:
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Example 2:
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
All Nodes will have unique values.
'''

def inorder_successor(root, target):
	#left - root - right
	# global found
	found = False
	def recursive_inorder(root, target):
		nonlocal found
		if root.left:
			left_res = recursive_inorder(root.left, target)
			if left_res:
				return left_res
		
		if found:
			return root.val
		if root.val == target:
			found = True
	
		if root.right:
			right_res = recursive_inorder(root.right, target)
			if right_res:
				return right_res
	return recursive_inorder(root, target)

'''
Method 2: inorder/DFS using explicit stack

[9, 20, 9 25]

'''
def inorder_explicit(root):
	'''
	inorder traversal (only) with explicit stack
	'''
	stack = []
	# found = False
	while len(stack) != 0 or root:
		while root:
			stack.append(root)
			root = root.left

		root = stack.pop()
		print(root.val)
		
		root = root.right

def inorder_successor_2(root, target):
	'''
	modified inorder traversal to find successor
	'''
	stack = []
	found = False
	
	while len(stack) != 0 or root:
		while root:
			stack.append(root)
			root = root.left

		root = stack.pop()
		if found:
			return root.val
		if root.val==target:
			found = True
		
		root = root.right 



'''
Method 3: Use BST property
Idea: If current node is less than the target, then we can discard the left subtree and move right
		If current node is greater than the target, then the current node is potentially the successor.
			Move to left child
			If left child is null, current successor is the right one

time: O(logn) average case, O(n) worst case (skewed BST)
space: O(logn)
'''

def inorder_successor_3(root, target):
	successor = None

	def recurse(root):
		if root: #if current node is not null, otherwise stop
			nonlocal target, successor
			if root.val <= target:
				recurse(root.right)
			else:
				successor = root.val
				recurse(root.left)

	recurse(root)
	return successor

'''
Method 4:
Same idea as method 3, but using iteration to reduce space complexity
time: O(logn) avg case, O(n) worst case
space: O(1)
'''

def inorder_successor_4(root, target):
	successor = None
	while root:
		if root.val <= target:
			root = root.right
		else:
			successor = root.val
			root = root.left
	return successor


from tree_base import Node

tree = Node(20, Node(9, Node(5), Node(12, Node(11), Node(14))), Node(25))

test = [20, 9, 5, 12, 11, 14, 25]
for i in test:
	print(f'{i} -> {inorder_successor_4(tree, i)}')

# print(inorder_explicit(tree))