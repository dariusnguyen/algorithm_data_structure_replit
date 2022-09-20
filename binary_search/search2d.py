'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix "matrix". This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

'''

'''
UMPIRE
U
	Any constraints on m and n?
	Can the matrix contain duplicate values?
M
	Binary search
P
	pretend search is performed on an array of len m*n
	index i of the array is converted to cell index (5//n, 5%n)

	run binary search
	mid = low + (high-low)/2 #prevent overflow for large m, n
	if position corresponding to mid in the matrix contains target
		return true
	else if mid value <target
		search(target, low, mid-1)
	else
		search(target, mid+1, high)
	
	time: O(log(m*n))
	space: O(1)

I
R
E

'''

def binary_search_2d(matrix, target):
	m = len(matrix)
	n = len(matrix[0])

	def binary_search(matrix, target, low, high):
		# print(f'low={low} high={high}')
		
		if high<low:
			return False
			
		mid = low + (high-low)//2
		mid_m = mid // n
		mid_n = mid % n
		
		if matrix[mid_m][mid_n] == target:
			return True
		elif target < matrix[mid_m][mid_n]:
			return binary_search(matrix, target, low, mid-1)
		elif matrix[mid_m][mid_n] < target:
			return binary_search(matrix, target, mid+1, high)
	
	return binary_search(matrix, target, 0, m*n-1)