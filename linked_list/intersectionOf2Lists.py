'''
Write a program to find the node at which the intersection of two singly linked lists begins. For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.
'''

'''
UMPIRE
U
	Can the 2 lists not have an intersection?
		Yes, return None
	Can the list have more than 1 beginnings of intersections?
		No
	Constraints on time/memory?
		O(n) time
		O(1) mem
M
	Linked list
	Multiple pass
P
	the parts of the 2 lists that intersect must have the same length, so first need to make them have the same length by cutting of the "prefix"

	function get_len(head):
		if last node
			return 1
		return 1 + get_len(next node)

	get_len(headA)
	get_len(headB)

	check which list is longer
	iteratively reduce the length of the longer list until they are equal in length
	traverse the 2 lists and check if they point to the same node at any point
I
R
E
	Time: O(m + n + m(or n) + m + n) = O(m+n)
'''

def get_intersection(headA, headB):
	def get_len(head):
		if head.next is None:
			return 1
		return 1 + get_len(head.next)

	lenA = get_len(headA)
	lenB = get_len(headB)
	
	if lenA > lenB:
		long_len, short_len = lenA, lenB
		long_head, short_head = headA, headB
	else:
		long_len, short_len = lenB, lenA
		long_head, short_head = headB, headA

	while long_len > short_len:
		long_len -= 1
		long_head = long_head.next

	while long_head != short_head:
		long_head = long_head.next
		short_head = short_head.next

	return(str(long_head))