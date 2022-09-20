# from trees.tree_base import Node

def printLeaves(root):
	stack = [root] #DFS

	while stack:
		curr = stack.pop()
		# preorder: check root first, then left, then right
		if curr.left is None and curr.right is None:
			print(curr.val)
		else:
			if curr.right:
				stack.append(curr.right)
			if curr.left:
				stack.append(curr.left)

def returnLeaves(root):
	# DFS preorder: root left right
	stack = [root]
	res = []
	while stack:
		curr = stack.pop()
		if curr.left is None and curr.right is None:
			res.append(curr.val)
		else:
			if curr.right:
				stack.append(curr.right)
			if curr.left:
				stack.append(curr.left)
	return res
				
				


			
			
			



	
		