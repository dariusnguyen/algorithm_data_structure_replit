'''

'''
def countGroups(related):
	def dfs(cell):
		nonlocal visited, grid, count, visited_rows
		stack = [cell]
		while stack:
			r, c = stack.pop()
			visited.add((r,c))
			if grid[r][c] == '1':
				newR = c
				if newR not in visited_rows:
					visited_rows.add(newR)
					for newC in range(len(grid[0])):
						# if (newR, newC) not in visited:
						stack.append((newR,newC))

	visited = set()
	visited_rows = set()
	count = 0
	grid = related

	for r in range(len(related)):
		for c in range(len(related[0])):
			if (r,c) not in visited and r not in visited_rows and related[r][c] == '1':
				count += 1
				dfs((r,c))

	return count

related = ['1000001000', '0100010001', '0010100000', '0001000000', '0010100000', '0100010000', '1000001000', '0000000100', '0000000010', '0100000001']

print(countGroups(related))