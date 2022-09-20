'''
DFS
Preorder: Root - Left - Right
'''

def preorder(root, traversal = []):
	if root:
		traversal.append(root.val)
		preorder(root.left, traversal)
		preorder(root.right, traversal)
		
	return traversal

def preorder_iter(root):
	stack = [root]
	res = []
	while stack:
		curr = stack.pop()
		res.append(curr.val)
		if curr.right:
			stack.append(curr.right)
		if curr.left:
			stack.append(curr.left)
	return res
'''
DFS
Inorder: left root right
'''

def inorder(root, traversal = []):
	if root:
		inorder(root.left, traversal)
		traversal.append(root.val)
		inorder(root.right, traversal)
	return traversal

def inorder_iter(root):
	'''
 	starting at the root, move left as far as you can while pushing left nodes onto the stack
  	once you have reached None (can't go left anymore), you are done with the left subtree
   		pop from the stack and assign to curr
	 	append curr to result
   		move right by assigning curr=curr.right
   
 	'''
	stack = []
	curr = root
	res = []
	while stack or curr:
		if curr:
			stack.append(curr)
			curr = curr.left
		else:
			curr = stack.pop()
			res.append(curr.val)
			curr = curr.right
	return res

		
		
'''
DFS
Postorder: left right root
'''

def postorder(root, traversal = []):
	if root:
		postorder(root.left, traversal)
		postorder(root.right, traversal)
		traversal.append(root.val)
	return traversal

def postorder_iter(root):
	'''
	https://www.geeksforgeeks.org/iterative-postorder-traversal/  	
 	'''
	stack1 = [root]
	stack2 = []
	# res = []
	# curr = root

	while stack1:
		curr = stack1.pop()
		stack2.append(curr)
		if curr.left:
			stack1.append(curr.left)
		if curr.right:
			stack1.append(curr.right)
		
	stack2.reverse()
	return [i.val for i in stack2]