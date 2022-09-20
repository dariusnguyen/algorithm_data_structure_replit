'''
108. Convert Sorted Array to Binary Search Tree
Easy

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
'''

'''
use recursion
base case: root is a leaf
	return root
else
	find middle element and use it as root
 	root.left = recurse(:middle index -1)
  	root.right = recurse(right index + 1:)
'''

from trees.tree_base import Node

def sortedArray2BST(arr):
	def recurse(arr, l, r):	
		if l == r:
			return Node(arr[l])
		if l > r:
			return None
	
		mid = int((l+r)/2)
		root = Node(arr[mid])
		print('l, r, root val:', l, r, arr[mid])
		root.left = recurse(arr, l, mid-1)
		root.right = recurse(arr, mid+1, r)
		return root

	return recurse(arr, 0, len(arr)-1)
	