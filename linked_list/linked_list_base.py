class Node():
	def __init__(self, data, next=None, prev=None):
		self.data = data
		self.prev = prev
		self.next = next
		
	def __str__(self):
		if self.next:
			next_val = self.next.data
		else:
			next_val = None
		s = f'Node({self.data}), next=Node({next_val}), prev=Node({self.prev.data})'
		return s
		
	# def print_list(self):
	# 	curr = self
	# 	while curr:
	# 		print(f'{curr.data} -> ', end='')
	# 		curr = curr.next
	# 	print('None')

	def print_list(self):
		curr = self
		while curr:
			next_node = curr.next
			print(f'{curr.data}', end='')
			if next_node and next_node.prev == curr:
				print(' <-> ', end='')
			else:
				print(' -> ', end='')
			curr = curr.next
		print('None')


