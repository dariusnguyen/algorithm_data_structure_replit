from linked_list import linked_list_base as llb
def add(headA, headB):
	dummy = llb.Node('dummy')
	curr = dummy
	carry = 0
	while(headA or headB):
		if headA and headB:
			carry, new_data = divmod(headA.data + headB.data + carry, 10)
			curr.next = llb.Node(new_data)
			headA = headA.next
			headB = headB.next
		elif headA:
			carry, new_data = divmod(headA.data + carry, 10)
			curr.next = llb.Node(new_data)
			headA = headA.next
		else:
			carry, new_data = divmod(headB.data + carry, 10)
			curr.next = llb.Node(new_data)
			headB = headB.next
		curr = curr.next

	dummy.next.print_list()
	