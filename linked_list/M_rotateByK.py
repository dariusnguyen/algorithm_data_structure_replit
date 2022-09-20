'''
61. Rotate List
Medium

Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]
'''

'''
2 pointers
move p1 by k steps
move p1 and p2 until p1 reaches the end node
	save node before p1
for k steps:
	point end node.next to head node
'''

def rotate(head, k):
	p1 = head.next
	p2 = head
	beforeP1 = head
	for i in range(k-1):
		p1 = p1.next
		beforeP1 = beforeP1.next
	while p1.next:
		p1 = p1.next
		p2 = p2.next
		beforeP1 = beforeP1.next

	curr = p2
	for i in range(k):
		p2 = p2.next
		p1.next = head
		beforeP1.next = None
		head = p1