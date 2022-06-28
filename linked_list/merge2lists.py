'''
Problem #3: Merge Two Sorted Lists
Merge two sorted linked lists.

Examples:

Input: 1->2->4, 1->3->4  
Output: 1->1->2->3->4->4


2 pointers
init A = headA
A = headB

while A is True or B is True
	if B is None (then A must be not None)		
		curr = A
		A = A.next
	else (B is not None)
		if A is None	
			curr = B
			B = B.next
		else (A is also not None)
			if A<B:
				curr = A
				A = A.next
			else
				curr = B
				B = B.next

	if B is None or (A is not None and A<B)
		curr = A
		A = A.next
	else A is not None and B>=A
		if A is None	
			curr = B
			B = B.next
		else (A is also not None)
			if A<B:
				curr = A
				A = A.next
			else
				curr = B
				B = B.next
return headA or headB, whichever is smaller

'''

def merge(headA, headB):
	# if headA is None:
	# 	if headB is None:
	# 		return None
	# 	return headB
	# if headB is None:
	# 	return headA

	A = headA
	B = headB

	# head = A if headA.data < headB.data else B
	dummy = Node('dummy', None)
	curr = dummy
	
	while (A or B):
		if B is None:
			curr.next = A
			A = A.next
		else:
			if A is None:
				curr.next = B
				B = B.next
			else:
				if A.data < B.data:
					curr.next = A
					A = A.next
				else:
					curr.next = B
					B = B.next		
		curr = curr.next

	dummy = dummy.next
	while dummy is not None:
		print(dummy.data, end=' ')
		dummy = dummy.next
	