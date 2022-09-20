'''
98. Validate Binary Search Tree
Medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than OR EQUAL TO the node's key.
The right subtree of a node contains only nodes with keys greater than OR EQUAL TO the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 
Constraints:
The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''

def isValidBST_1(root, lower = -float('inf'), upper = float('inf')):
	'''
	Method 1: Recursive traversal with upper and lower bounds
	
	recursive f()
	traverse the tree with pre-order (top-down DFS)
	root -> left -> right
	
	init lower = -inf
		upper = +inf
	base case:
		if root <= lower bound or root >= upper bound
			return False
		(else)
		return f(upper = root.val) on left child AND f(lower = root.val) on right child
	
	time: O(n) where n is num nodes in tree
	space: O(n) due to recursive call stack
	'''
	
	if root.val < lower or root.val > upper:
		return False

	if root.left:
		left_res = isValidBST_1(root.left, lower = lower, upper = root.val)
	else:
		left_res = True

	if root.right:
		right_res = isValidBST_1(root.right, lower = root.val, upper = upper)
	else:
		right_res = True
		
	return left_res and right_res

def isValidBST_2(root):
	'''
	Method 2: Iterative traversal with upper and lower bounds

	Similar to method 1, but using iteration and an explicit stack for DFS

	init stack with root
	while stack is not empty
		pop from stack
		check if node > upper and node < lower
			return false

		update upper and lower
		check node.left and node.right

	time: O(n)
	space: O(n)
	'''

	stack = [(root, -float('inf'), float('inf'))]

	while len(stack) != 0:
		curr, lower, upper = stack.pop()
		if curr.val < lower or curr.val > upper:
			return False

		if curr.left:
			stack.append((curr.left, lower, curr.val))
		if curr.right:
			stack.append((curr.right, curr.val, upper))

	return True


def isValidBST_3(root):
	'''
	Method 3: Recursive inorder traversal

	Idea: Inorder traversal: left, root, right
	The values of the visited nodes have to be in increasing order. If we find a value that is out of order, then the BST is invalid
	Use a global variable last to save the last visited node value
	
	recursive f(root)
	with external 'last' variable
	if root.left exists
		if f(root.left)==False
			return False
	if root < last
		return False

	if root.right exists
		return f(root.right)

	return True
	'''
	global last
	last = -float('inf')
	
	def inorder(root):
		global last
		if root.left:
			if inorder(root.left)==False:
				return False
				
		if root.val < last:
			return False
		last = root.val
		
		if root.right:
			return inorder(root.right)
			
		return True

	return inorder(root)