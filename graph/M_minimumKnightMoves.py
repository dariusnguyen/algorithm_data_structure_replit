'''
1197. Minimum Knight Moves
Medium

In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

 
Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]

Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]

'''

'''
source 0 0
target 5 5

0 0 -> 0 1 -> 2 1
      x, y+1
	  		 x+2 y

0 0 - 1 2 - 3 3 - 5 4 - 6 6
0 0 - 2 1 - 4 2 - 3 

0 1 2 3 4 5
1        
2       .
3
4
5

recursion
explore graph w BFS
keep track of visited cells
track number of steps using count
return once find the target

optimize with DP
'''

def minKnightMoves_1(x, y):
	visited = set()
	q = [(0,0,0)]
	directions = [(1,2), (2,1), (-1,-2), (-2,-1), (-1,2), (-2,1), (1,-2), (2,-1)]
	# minSteps = 0
	while q:
		currx, curry, steps = q.pop(0)
		# print(currx, curry, steps)
		visited.add((currx, curry))
		for newx, newy in [(currx+i, curry+j) for i, j in directions]:
			if (newx, newy) == (x, y):
				# minSteps = min(steps + 1, minSteps)
				return steps + 1
			elif (newx, newy) not in visited:
				q.append((newx, newy, steps + 1))

def minKnightMoves_2(x, y):
	'''
 	use 2 concurrent BFS, one from source and one from target
 	'''
	qSource = [(0,0,0)]
	qTarget = [(x,y,0)]
	visitedSource = {}
	visitedTarget = {}
	directions = [(1,2), (2,1), (-1,2), (2,-1), (1,-2), (-2,1), (-1,-2), (-2,-1)]

	while True:
		currX, currY, steps = qSource.pop()
		if (currX, currY) in visitedTarget:
			return steps + visitedTarget[(currx, curry)]

		currXT, currYT, stepsT = qTarget.pop()
		if (currXT, currYT) in visitedSource:
			return stepsT + visitedSource[(currXT, currYT)]
			
		for i, j in directions:
			newX = currX + i
			newY = currY + j
			if (newX, newY) not in visitedSource:
				visitedSource[(newX, newY)] = steps + 1

			newXT = currXT + i
			newYT = currYT + j
			if (newX, newY) not in visitedTarget:
				visitedTarget[(newXT, newYT)] = stepsT + 1
		
		

	
print(minKnightMoves(2, 1))