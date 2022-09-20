'''
257. Binary Tree Paths

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:
Input: root = [1]
Output: ["1"]
'''

'''
Method 1: use a stack to store path

Traverse the tree using DFS preorder root left right
use a stack to keep track of current path
once reaching a leaf, the whole stack represents a path
	push the leaf node
	add that path to result
 	pop the leaf node

'''

def binaryTreePaths(root):
	def inorder(root):
		if root:
			stack.append(root.val)
			if root.left is None and root.right is None:
				res.append(stack.copy())
			else:
				inorder(root.left)
				inorder(root.right)
			
			stack.pop()
	
	stack = []
	res = []			
	inorder(root)
	return res

'''
Method 2: same idea as method 1, but use a 'path' variable to pass down from parent to children instead of a stack

'''

def binaryTreePaths_2(root):

	def inorder(root, path=[]):
		path = path.copy() # make a new copy of path to avoid referencing the same 'path' object again
		if root:
			path.append(root)

			if root.left is None and root.right is None:
				res.append(path.copy())
			else:
				inorder(root.left, path)
				inorder(root.right, path)

	res = []
	inorder(root)
	return res
				