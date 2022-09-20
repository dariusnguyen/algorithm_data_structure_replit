'''
https://leetcode.com/discuss/interview-question/1431720/Cisco-or-Online-Assessment-or-Software-Engineer-Master's-(Intern)-United-States

Cisco SWE OA

write a function that returns a chessboard pattern
"B" for black squares, "W" for white squares
The function takes N as input and generates the board.

Example:
Input: 5
Output:
W B W B W
B W B W B
W B W B W
B W B W B
W B W B W

Explanation: Size of the chessboard is 5 and the top left square will always be white
'''

'''
UMPIRE

Understand
	N is both number of columns and number of rows
	Corner cases:
		N<1: return empty board
		N=1: board with 1 square?
	Question: Does the function only need to print out the board, or also return it? If return it, in what format? List?


Match


Plan
	2 loops
	for each row
		for each column
			if last = ''
				if row is odd
					print W
					last = W
				else
					print B
					last = B
			else if last =='B'
				print W
			else
				print B

Time: O(n^2)
Space: O(1)

Method 2:
if n<1:
	print()
if n==1:
	print W
if n>1:
	generate even row
	generate odd row
	for each row index
		if row is even
			print even row
		else
			print odd row

Time: O(n+n+n) = O(n)
Space: O(n+n) = O(n)
	


Implement
'''
def chess_board(n: int):
# 	if n<1:
# 		print()
# 		return None
# 	last = ''
# 	for i in range(n):
# 		for j in range(n):
# 			if i==0 and j==0:
# 				print('W ')
# 				last = 'W'
# 			else:
# 				if last=='W':
# 					print('B ')
# 					last = 'B'
# 				else:
# 					print('W ')
# 					last = 'W'

	if n<1:
		print()
	if n==1:
		print('W')
	else:
		even = ' '.join(['W' if i%2==0 else 'B' for i in range(n)])
		odd = ' '.join(['B' if i%2==0 else 'W' for i in range(n)])
		for i in range(n):
			if i%2==0:
				print(even)
			else:
				print(odd)
'''
Review

Evaluate
'''