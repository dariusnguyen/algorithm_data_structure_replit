
def reverse_3_nodes(head):
	#edge case: there are only 2 nodes in the list
	if head and head.next and head.next.next is None:
		n1 = head
		n2 = head.next
		n1.next = n2.next
		n2.next = n1
		n1.prev = n2
		return n2
		# n1 <-> n2 <-> None
		# n2 <-> n1 <-> None
		
	#edge case: there is only 1 node in the list
	if head and head.next is None:
		return head

	#edge case: the list is empty
	if head is None:
		return -1

	#init n1 to head
	n1 = head
	# save n1.next.next to new_head as this will be the new head of the revesed list	
	new_head = n1.next.next
	#init end_node_last3 to None
	end_node_last3 = None
	# i=0
	while n1 and n1.next and n1.next.next:
		#since we have found 3 consecutive nodes in the while condition, save n1.next and n2.next to n2 and n3		
		n2 = n1.next
		n3 = n2.next

		#begin swapping
		# n1 <-> n2 <-> n3 <-> n3.next
		# n3 <-> n2 <-> n1  -> n3.next
		
		n1.next = n3.next #required for n1 = n1.next later
		n3.next = n2
		n2.prev = n3
		n2.next = n1
		n1.prev = n2

		first_node_this3 = n3

		#link the end node from the last iteration to n3
		if end_node_last3:
			end_node_last3.next = first_node_this3
		first_node_this3.prev = end_node_last3

		#save n1 as the new end node
		end_node_last3 = n1

		#advance n1 for the next iteration
		n1 = n1.next
		
		# print(f'end of iteration {i}')	
		# i+=1
		
	#after the loop finishes, check if there are 2 nodes remaining and swap them
	if n1 and n1.next and n1.next.next is None:		
		n2 = n1.next

		# n1 <-> n2 <-> None
		# n2 <-> n1 <-> None
		n1.next = n2.next #n2.next should be None
		n2.next = n1
		n1.prev = n2

		
		end_node_last3.next = n2
		n2.prev = end_node_last3
		
		# print(f'swapped last 2 nodes')
		# print(f'end_node_last3 = {end_node_last3}')
		# print(f'n1 = {n1} n2 = {n2}')

	elif n1 and n1.next is None:
		end_node_last3.next = n1
		n1.prev = end_node_last3
		
		
				
	return new_head