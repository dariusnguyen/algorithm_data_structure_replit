'''
In a given grid of 0s and 1s, we have some starting row and column sr, sc and a target row and column tr, tc. Return the length of the shortest path from sr, sc to tr, tc that walks along 1 values only.

Each location in the path, including the start and the end, must be a 1. Each subsequent location in the path must be 4-directionally adjacent to the previous location.

It is guaranteed that grid[sr][sc] = grid[tr][tc] = 1, and the starting and target positions are different.

If the task is impossible, return -1.

Examples:

input:
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: 8
(The lines below represent this grid:)
1111
0001
1111

grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 1, 1]]
sr = 0, sc = 0, tr = 2, tc = 0
output: -1
(The lines below represent this grid:)
1111
0001
1011
Constraints:

[time limit] 5000ms
[input] array.array.integer grid
1 ≤ arr.length = arr[i].length ≤ 10
[input] integer sr
[input] integer sc
[input] integer tr
[input] integer tc
All sr, sc, tr, tc are valid locations in the grid, grid[sr][sc] = grid[tr][tc] = 1, and (sr, sc) != (tr, tc).
[output] integer
'''

'''
Shortest path in unweighted graph => BFS
in the queue, use a variable to track the length of the path
q = [sr, sc, 0]
while q is not empty
	r, c, path = q.pop
	if r, c is target cell
 		return path
 	loop through neighbors
  		if neighbors are valid (within bounds, not in visited, contains 1)
			add to queue
   			to avoid using a visited set (consuming extra space) update visited 1 to -1
(after exhausting all paths) return -1
'''

from queue import Queue


def shortestCellPath(grid, sr, sc, tr, tc):
	q = Queue()
	q.put([sr, sc, 0])

	while q:
		r, c, pathLen = q.get()
		for i, j in [[0,1], [1,0], [0, -1], [-1,0]]:
			newR = r + i
			newC = c + j
			if newR>=0 and newR<len(grid) and newC>=0 and newC<len(grid[0]) and grid[newR][newC]==1:
				if newR==tr and newC==tc:
					return pathLen + 1
				q.put([newR, newC, pathLen + 1])
				grid[newR, newC] = -1
	return -1


				
			

	
	

