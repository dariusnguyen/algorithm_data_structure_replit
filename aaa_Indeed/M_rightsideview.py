'''
199. Binary Tree Right Side View
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,null,3]
Output: [1,3]

Example 3:

Input: root = []
Output: []
'''

'''
UMPIRE
*U
		1
	2		3
4		
In this case, is the rightside view 1,3,4? Yes

*M
tree
level order traversal/bfs
*P
use a queue for bfs
after completing the traversal at each level, add rightmost node to result
Time: O(n)
Space: O(n) ?
*I
*R
*E

'''
class Node():
	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right
	def __str__(self):
		return f'Node({self.data})'
		
def rightsideview(root):
	'''
	This solution considers the right as the front of the queue
	and the left as the back of the queue
	So q.pop() is used to dequeue
	and q.insert(0, node) is used to enqueue
	The for loop is used to traverse all nodes in the current level
	'''
	q = [root]
	res = []
	while len(q)>0:
		res.append(q[0])
		for i in range(len(q)):
			curr = q.pop()
			if curr.left:
				q.insert(0, curr.left)
			if curr.right:
				q.insert(0, curr.right)
	# for i in res:
	# 	print(i, end=' ')
	return [str(i) for i in res]

def rightSideView2(root):
	'''
	Same idea as the above solution
	but here we consider the left as the front of the queue, and use q.pop(0) to dequeue
	and q.append(node) to enqueue to the right	
	'''
	q = [root]
	output = []
	while len(q) > 0:
		output.append(q[-1])
		for i in range(len(q)):			
			curr = q.pop(0)
			if curr.left:
				q.append(curr.left)
			if curr.right:
				q.append(curr.right)
	return output