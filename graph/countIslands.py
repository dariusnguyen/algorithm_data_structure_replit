'''
Problem #1: Island Problem
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Examples:

Input:
11110
11010
11000
00000

Output:  1

Input:
11000
11000
00100
00011

Output: 3
'''

'''
init visited list
loop through the grid using nested loop
	if cell contains a 1 and not in visited
 		increment count
   		explore island using dfs

dfs function:
	while stack is not empty
 		pop from stack
   		add cell to visited
	 	if neighbor is 1
   			add neighbors to stack	  
'''

def countIslands(grid):
	def dfs(grid, cell):
		nonlocal visited
		stack = [cell]
		while stack:
			r, c = stack.pop()
			visited.append((r,c))
			if grid[r][c] == 1:
				for newr, newc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
					if newr<len(grid) and newr>=0 and newc<len(grid[0]) and newc>=0 and (newr, newc) not in visited:
						stack.append((newr, newc))
						# print(f'append {(newr, newc)}')

	visited = []
	count = 0

	for r in range(len(grid)):
		for c in range(len(grid[0])):
			# print((r,c))
			if (r,c) not in visited and grid[r][c] == 1:
				count += 1
				# print((r,c), f'count={count}')
				dfs(grid, (r, c))
				# print('visited', visited)
				
				
	return count


grid = [[1,1,1,1,0],
		[1,1,0,1,0],
		[1,1,0,0,0],
		[0,0,0,0,0]]

print(countIslands(grid))

grid2 = [[1,1,0,0,0],
		[1,1,0,0,0],
		[0,0,1,0,0],
		[0,0,0,1,1]]
print(countIslands(grid2))
# for c in grid:
# 	if c=='\n':