class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next
		
	def __str__(self):
		return f'Node({self.data})'
		
	def print_list(self):
		curr = self
		while curr:
			print(f'{curr.data} -> ', end='')
			curr = curr.next
		print('None')