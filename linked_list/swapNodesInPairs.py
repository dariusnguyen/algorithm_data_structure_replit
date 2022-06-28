'''
https://leetcode.com/problems/swap-nodes-in-pairs/
24. Swap Nodes in Pairs
Medium

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]
 

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''

'''
Method 1: Iterative

loop until reach the end of the list
use 2 pointers: n1 and n2
swap 2 nodes
after swapping, link node before n1 (previous_node) to n2
'''

from linked_list.linked_list_base import Node

def swap_pairs_iterative(head: Node):
	#edge case
	if head is None or head.next is None:
		return head
	
	previous_node = None #init previous_node to None
	n1 = head #init n1 to head of list
	new_head = head.next #new_head is the new head of the list, to be returned by this function
	
	while n1 and n1.next:
		#save n1.next to n2
		n2 = n1.next
		
		#swap n1 and n2
		n1.next = n2.next
		n2.next = n1

		#if there is a previous_node, point previous_node.next to n2
		if previous_node:
			previous_node.next = n2

		#swapping complete, move previous_node to n1 and move n1 to the next pair for the next swap
		previous_node = n1
		n1 = n1.next
		
	return new_head


'''
Method 2: recursive

Idea:
	1. At the current node, swap it with the next node.
	2. Point its next node to the result of the recursive call on the remaining of the list
	Base case: when reached the end (curr is None or curr.next is None, just return curr without swapping)

'''
def swap_pairs_recur(head: Node):
	#base case
	if head is None or head.next is None:
		return head
		
	#init 2 pointers
	n1 = head
	n2 = head.next

	#swap
	n1.next = swap_pairs_recur(n2.next) #point n1.next to the result of the recursive call on the remaining of the list
	n2.next = n1

	#return n2 because it is the new "head"
	return n2