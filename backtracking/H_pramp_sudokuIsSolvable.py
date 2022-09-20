def isSolvable(board):
	n = 9
	rows = [set() for _ in range(n)]
	cols = [set() for _ in range(n)]
	boxes = [set() for _ in range(n)]

	def getBox(r, c): #return box index from a given row, column pair
		return r//3*3 + c//3

	def nextCell(r, c):
		#return the next row, column index given the current row, column
		#the next row can be out of bounds, but will be checked in the recurse(function)
		nextC = c + 1
		nextR = r
		if c == n - 1:
			nextC = 0
			nextR = r + 1
		return nextR, nextC
		
	def getCandidates(r, c): #check all possible candidates and return only the ones valid for current row, column
		candidates = set()
		for i in range(1,10):
			if i in rows[r] or i in cols[c] or i in boxes[getBox(r,c)]:
				continue
			else:
				candidates.add(i)
		return candidates
				
	def place(r, c, num): #place num in row, column and update corresponding sets
		board[r][c] = num
		rows[r].add(num)
		cols[c].add(num)
		boxes[getBox(r,c)].add(num)

	def remove(r, c, num): #remove num from row, column to backtrack
		board[r][c] = '.'
		rows[r].remove(num)
		cols[c].remove(num)
		boxes[getBox(r,c)].remove(num)

	def init(): #initialize the board by populating sets with cells already filled
		for r in range(n):
			for c in range(n):
				if board[r][c] != '.':
					place(r, c, int(board[r][c]))
		
	def recurse(r, c): #main function with recursion logic
		if r >= n: #if r is out of bounds, then all cells have been filled
			return True
		if board[r][c] == '.': #if current cell is empty, try to fill it
			candidates = getCandidates(r, c)
			if len(candidates) == 0:
				return False
			for i in candidates:
				place(r, c, i)
				
				nextR, nextC = nextCell(r, c)
				if recurse(nextR, nextC):
					return True
				remove(r, c, i)
			return False #all candidates have been tried, but still unsuccessful, so board not solvable
		else: #current cell is already filled, proceed with next cell
			nextR, nextC = nextCell(r, c)
			return recurse(nextR, nextC)

	init()
	return recurse(0, 0)

board0 = [[ 5 , 3 ,'.','.', 7 ,'.','.','.','.'],
		 [ 6 ,'.','.', 1 , 9 , 5 ,'.','.','.'],
		 ['.', 9 , 8 ,'.','.','.','.', 6 ,'.'],
		 [ 8 ,'.','.','.', 6 ,'.','.','.', 3 ],
		 [ 4 ,'.','.', 8 ,'.', 3 ,'.','.', 1 ],
		 [ 7 ,'.','.','.', 2 ,'.','.','.', 6 ],
		 ['.', 6 ,'.','.','.','.', 2 , 8 ,'.'],
		 ['.','.','.', 4 , 1 , 9 ,'.','.', 5 ],
		 ['.','.','.','.', 8 ,'.','.', 7 , 9 ]]


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
	print(sudoku_solve(i))