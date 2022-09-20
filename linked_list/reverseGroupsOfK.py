'''
head: head of current list
ptr: pointer for iteration
rev_head: head of reversed list


'''

def reverse(head):
	'''reverse the entire list'''
	new_head = None
	curr = head
	while curr:
		#save curr.next to next so we can move to the next node later
		next = curr.next

		#point curr.next to new_head
		curr.next = new_head
		#new_head now becomes curr
		new_head = curr

		#move curr to the next node in the list
		curr = next

	return new_head

def reverse(head, k):
	'''reverse only k nodes in the list, assuming there are at least k nodes'''
	new_head = None
	curr = head
	for _ in range(k):
		#save curr.next to next so we can move to the next node later
		next = curr.next

		#point curr.next to new_head
		curr.next = new_head
		#new_head now becomes curr
		new_head = curr

		#move curr to the next node in the list
		curr = next

	return new_head
	
		
	
from linked_list.linked_list_base import Node

class Solution:
    
    def reverseLinkedList(self, head, k):
        
        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains 
        # atleast k nodes.
        new_head, ptr = None, head #new_head = None, ptr = 1
        while k: #k=3
            
            # Keep track of the next node to process in the
            # original list
            next_node = ptr.next #next_node = 1.next = 2
            
            # Insert the node pointed to by "ptr"
            # at the beginning of the reversed list
            ptr.next = new_head #ptr.next = None
            new_head = ptr #new_head = 1
            
            # Move on to the next node
            ptr = next_node #ptr = 2
            
            # Decrement the count of nodes to be reversed by 1
            k -= 1
        
        # Return the head of the reversed list
        return new_head
                
    
    def reverseKGroup(self, head: Node, k: int) -> Node:
        
        count = 0
        ptr = head
        
        # First, see if there are atleast k nodes
        # left in the linked list.
        while count < k and ptr:
            ptr = ptr.next
            count += 1
        
        # If we have k nodes, then we reverse them
        if count == k: 
            
            # Reverse the first k nodes of the list and
            # get the reversed list's head.
            reversedHead = self.reverseLinkedList(head, k)
            
            # Now recurse on the remaining linked list. Since
            # our recursion returns the head of the overall processed
            # list, we use that and the "original" head of the "k" nodes
            # to re-wire the connections.
            head.next = self.reverseKGroup(ptr, k)
            return reversedHead
        return head