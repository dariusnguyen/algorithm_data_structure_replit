class Node():
	def __init__(self, val, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right
	def __str__(self):
		res = f'Node({self.val})'
		# if self.left:
		# 	res += f', L: Node({self.left.val})'
		# else:
		# 	res += ', L: None'
		# if self.right:
		# 	res += f', R: Node({self.right.val})'
		# else:
		# 	res += ', R: None'
			
		return res
	def __repr__(self):
		# return f'Node({self.val})' #, L: Node({self.left.val}), R: Node({self.right.val})'
		return str(self.val)
		