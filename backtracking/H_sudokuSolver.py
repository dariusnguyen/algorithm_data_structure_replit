'''
init()
	create sets
	loop through board and populate sets
nextCell(r, c)
	calc next column
	return next cell
getBox(r, c)
	r//3 * 3 + c//3
getCandidates(r, c)
	create candidates set
	loop through 1 - 9
 		if i not in row, col, box
   			add i to candidates
place(r, c, num)
	update board r, c
 	add num to appropriate sets
remove(r, c, num)
	update board r, c
 	remove num from sets
recurse(r, c)
	if r>=n
 		return True
   	if curr cell is empty
		getCandidates
  		for each candidate
			place() candidate
   			get nextCell()
   			if recurse(next cell) returns True
	  			return True
	  		else
	 			remove() to backtrack
	 	return False because all options exhausted
    else
		get nextCell()
  		return recurse(nextCell)
'''

class sudokuSolver:
	def __init__(self, board):
		self.board = board
		self.n = len(self.board)
		self.rows = [set() for _ in range(self.n)]
		self.cols = [set() for _ in range(self.n)]
		self.boxes = [set() for _ in range(self.n)]

		for r in range(self.n):
			for c in range(self.n):
				if self.board[r][c] != '.':
					self.place(r, c, self.board[r][c])
					
		print('Original board:')
		self.printBoard()

	def nextCell(self, r, c):
		nextR = r
		nextC = c + 1
		if c == self.n - 1:
			nextR = r + 1
			nextC = 0
			
		return nextR, nextC

	def getBox(self, r, c):
		box_n = self.n // 3
		return r//box_n * box_n + c // box_n

	def getCandidates(self, r, c):
		candidates = set()
		for i in range(1, self.n+1):
			i = str(i)
			if not (i in self.rows[r] or i in self.cols[c] or i in self.boxes[self.getBox(r, c)]):
				candidates.add(i)
		return candidates

	def place(self, r, c, num):
		self.board[r][c] = num
		self.rows[r].add(num)
		self.cols[c].add(num)
		self.boxes[self.getBox(r, c)].add(num)

	def remove(self, r, c, num):
		self.board[r][c] = '.'
		self.rows[r].remove(num)
		self.cols[c].remove(num)
		self.boxes[self.getBox(r, c)].remove(num)

	def recurse(self, r, c):
		if r >= self.n:
			return True
		if self.board[r][c] != '.':
			nextR, nextC = self.nextCell(r, c)
			return self.recurse(nextR, nextC)
		else:
			candidates = self.getCandidates(r, c)
			if len(candidates) == 0:
				# print(f'No candidates possible for {r,c}')
				return False
			
			for i in candidates:
				self.place(r, c, i)
				nextR, nextC = self.nextCell(r, c)
				if self.recurse(nextR, nextC):
					return True
				else:
					self.remove(r, c, i)
			# print(f'Exhausted all candidates {candidates} for {r, c}')
			return False

	def printBoard(self):
		for r in range(self.n):
			for c in range(self.n):
				print(self.board[r][c], end=' ')
			print()
		
	def solve(self):
		if self.recurse(0,0):
			print('Board has been solved:')
			self.printBoard()
		else:
			print('Board is not solvable!')


board0 = [["5","3",".",".","7",".",".",".","."],
		  ["6",".",".","1","9","5",".",".","."],
		  [".","9","8",".",".",".",".","6","."],
		  ["8",".",".",".","6",".",".",".","3"],
		  ["4",".",".","8",".","3",".",".","1"],
		  ["7",".",".",".","2",".",".",".","6"],
		  [".","6",".",".",".",".","2","8","."],
		  [".",".",".","4","1","9",".",".","5"],
		  [".",".",".",".","8",".",".","7","9"]]
# Output:	[["5","3","4","6","7","8","9","1","2"],
	# 		 ["6","7","2","1","9","5","3","4","8"],
	# 		 ["1","9","8","3","4","2","5","6","7"],
	# 		 ["8","5","9","7","6","1","4","2","3"],
	# 		 ["4","2","6","8","5","3","7","9","1"],
	# 		 ["7","1","3","9","2","4","8","5","6"],
	# 		 ["9","6","1","5","3","7","2","8","4"],
	# 		 ["2","8","7","4","1","9","6","3","5"],
	# 		 ["3","4","5","2","8","6","1","7","9"]]


board1 = [[".","8","9",".","4",".","6",".","5"],
		  [".","7",".",".",".","8",".","4","1"],
		  ["5","6",".","9",".",".",".",".","8"],
		  [".",".",".","7",".","5",".","9","."],
		  [".","9",".","4",".","1",".","5","."],
		  [".","3",".","9",".","6",".","1","."],
		  ["8",".",".",".",".",".",".",".","7"],
		  [".","2",".","8",".",".",".","6","."],
		  [".",".","6",".","7",".",".","8","."]]

board2 = [[".","2","3","4","5","6","7","8","9"],["1",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]

board3 = [[".",".","5",".",".","2",".",".","."],[".",".","9",".","4","7",".","2","."],[".",".","8",".","5","6",".",".","1"],[".",".",".",".",".","8","3","4","."],[".",".",".",".",".",".",".",".","6"],[".",".",".",".","3",".","1","8","."],[".","2",".",".",".",".",".",".","."],[".","9",".",".","8",".","6","7","."],["3",".","6","5","7",".",".",".","."]]

board4 = [[".",".","3","8",".",".","4",".","."],[".",".",".",".","1",".",".","7","."],[".","6",".",".",".","5",".",".","9"],[".",".",".","9",".",".","6",".","."],[".","2",".",".",".",".",".","1","."],[".",".","4",".",".","3",".",".","2"],[".",".","2",".",".",".","8",".","."],[".","1",".",".",".",".",".","5","."],["9",".",".",".",".","7",".",".","3"]]

board5 = [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]

for i in [board0, board1, board2, board4, board5]:
	newBoard = sudokuSolver(i)
	newBoard.solve()