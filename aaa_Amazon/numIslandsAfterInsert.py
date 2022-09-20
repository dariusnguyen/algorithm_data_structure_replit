'''
Suppose you are given a grid of 1's and 0's. All adjacent 1's are connected components.
For example, in the following case you have 2 connected components because you have two "islands" of 1's.

1 1 0 0 1 1
1 0 0 0 1 1 
1 0 0 0 0 0

Now you have a function called insertValue(coordinates) which takes in a row and column and inserts a 1. The function must return the updated number of connected components. So for example:
init:

1 1 0 0 1 1
1 0 0 0 1 1 
1 0 0 0 0 0

insertValue(row=1, col=1) gives 2 connected components still because grid is:

1 1 0 0 1 1
1 1 0 0 1 1 
1 0 0 0 0 0

insertValue(row=1, col=2) gives 2 connected components still because grid is:

1 1 0 0 1 1
1 1 1 0 1 1 
1 0 0 0 0 0
insertValue(row=1, col=3) gives 3 connected components because grid is:

1 1 0 0 1 1
1 1 1 1 1 1 
1 0 0 0 0 0
'''
def bfs(grid, x, y):
	num_rows, num_cols = len(grid), len(grid[0])
	visited = {}
	q = [(x,y)]
	islandID = 0
	while q:
		x, y = q.pop()
		if grid[x][y] == 1:
			visited[(x,y)] = islandID
			for i, j in [(1,0), (0,1), (-1,0), (0,-1)]:
				newX = x + i
				newY = y + j
				if newX > 0 and newX < num_cols-1 and newY > 0 and newY < num_rows-1 \
					and (newX, newY) not in visited:
					q.append((newX, newY))
		else:
			visited[(x,y)] = None
	islandID += 1
	return visited, 
					

def countIslands(grid):
	visited = {}
	q = []
	num_rows, num_cols = len(grid), len(grid[0])
	islandIndex = 0
	for i in range(num_rows):
		for j in range(num_cols):
			if grid[i][j] == 1:
				q.append((i, j))
				while q:
					curr = q.pop(0)
					x, y = curr[0], curr[1]
					
					if grid[x][y] == 1:
						visited[curr] = islandIndex						
						for i, j in [(1,0), (0,1), (-1,0), (0,-1)]:
							newX = x + i
							newY = y + j
							if newX > 0 and newX < num_cols-1 and newY > 0 and newY < num_rows-1 \
								and (newX, newY) not in visited:
								q.append((newX, newY))
					else:
						visited[curr] = None

				islandIndex += 1
	count = islandIndex + 1
	return count, visited

def insert1(x, y, grid, count, visited):
	num_rows, num_cols = len(grid), len(grid[0])
	
	if not (x > 0 and x < num_cols-1 and y > 0 and y < num_rows-1):
		raise 'Invalid insert position'
	
	adjacentIslands = set()
	
	for i, j in [(1,0), (0,1), (-1,0), (0,-1)]:
		newX = x + i
		newY = y + j
		if newX > 0 and newX < num_cols-1 and newY > 0 and newY < num_rows-1:
			if grid[newX][newY] == 1:
				adjacentIslands.add(visited[(newX, newY)])

	return count - len(adjacentIslands) + 1


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