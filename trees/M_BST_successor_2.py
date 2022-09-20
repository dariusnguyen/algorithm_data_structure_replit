'''
510. Inorder Successor in BST II
Medium

Given a node in a binary search tree, return the in-order successor of that node in the BST. If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

-------------------------
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
-------------------------

Example:
			5
		2	     11
	  1  4    7      12
                8
                  9
Input	Inorder successor
1		2
2		4
4		5
5		7
7		8
8		9
9		11

'''
'''
Optimal solution:
Idea:
if input node has a right child, then successor is the node in the right subtree with min value
if input node does not have a right child, then successor is the first node in the ancestor chain that has a left child where the left child is also an ancestor

Plan:
def function to get min node in the right subtree
	go right from root
	then go left as much as possible
if node has right child:
	successor = minRightSubtree()
if node does not have right child:
	traverse up the tree to the first ancestor with a left child
edge case: max node has no successor

time: O(h)
	worst case: right skewed BST = O(n)
	avg case: O(logn)
	where n is the number of nodes
space: O(1)

'''

class Node():
	def __init__(self, val, left=None, right=None, parent=None):
		self.val = val
		self.left = left
		self.right = right
		self.parent = parent
	def __str__(self):
		res = str(self.val)
		return res

def inorder_successor(inputNode):
	def minRightSubtree(root):
		while root:
			min = root
			root = root.left
		return min

	if inputNode.right: #case 1: inputNode has right subtree
		successor = minRightSubtree(inputNode.right)
	else:
		curr = inputNode
		while True:
			#case 3: inputNode is the maximum node in the BST
			#the ancestor chain of inputNode will lead to the root
			if curr.parent is None: 
				return None

			#case 2: successor is the first parent with a left child
			child = curr
			curr = curr.parent
			successor = curr
			if curr.left == child:
				break
	return successor
		
# BST = Node(20, Node(9, Node(5), Node(12, Node(11), Node(14))), Node(25))
n11 = Node(11)
n14 = Node(14)
n12 = Node(12, n11, n14)
n5 = Node(5)
n9 = Node(9, n5, n12)
n25 = Node(25)
n20 = Node(20, n9, n25)
n11.parent = n12
n14.parent = n12
n5.parent = n9
n12.parent = n9
n9.parent = n20
n25.parent = n20

BST = n20
'''
				20
		9				25
	5		12
		  11   14

20 -> 25
9 -> 11
5 -> 9
12 -> 14
11 -> 12
14 -> 20
25 -> None
'''
for i in [n20, n9, n5, n12, n11, n14, n25]:
	print(f'{i} -> {inorder_successor(i)}')

			
