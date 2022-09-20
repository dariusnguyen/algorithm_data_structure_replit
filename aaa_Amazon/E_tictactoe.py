'''
1275. Find Winner on a Tic Tac Toe Game
Easy

Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.

Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.

Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.

'''

'''
use 2 arrays, 1 for rows and 1 for cols
use 2 vars, 1 for diag and 1 for anti diag

loop through moves
	for each move, update corresponding elements in the row, col, diag and antidiag
 		if that element is 3 or -3 after update, then winner is found

if len(moves) = 9
	return draw
return pending
'''

def tictactoe(moves):
	rows = [0,0,0]
	cols = [0,0,0]
	diag = 0
	antidiag = 0
	
	for i, move in enumerate(moves):
		r = move[0]
		c = move[1]
		
		val = 1 if i%2==0 else -1
			
		rows[r] += val
		cols[c] += val
		
		if r==c:
			diag += val
		if r+c == 2:
			antidiag += val

		for line in [rows[r], cols[c], diag, antidiag]:
			if line == 3:
				return 'A'
			if line == -3:
				return 'B'
		
	return 'Draw' if len(moves) == 9 else 'Pending'


moves0 = [[0,0],[2,0],[1,1],[2,1],[2,2]]
moves1 = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
moves2 = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
moves3 = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2]]

print(tictactoe(moves0))
print(tictactoe(moves1))
print(tictactoe(moves2))
print(tictactoe(moves3))
