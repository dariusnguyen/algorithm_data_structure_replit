#!/bin/python3

#
# Complete the 'findSubmatrix' function below.
#
# Return an array with length 2, i.e. [width, height]
'''
BFS
search for 0
once find 0
DFS
'''

def isValid(matrix, r, c):
    if r<0 or c<0 or r>len(matrix)-1 or c>len(matrix[0])-1:
        return False
    return True

def findSubmatrix(matrix):
	m = matrix
	q = [(0,0)]
	all_r = []
	all_c = []
	visited = []
	while len(q)!=0:
		r, c = q.pop()
		if (r, c) not in visited:
			# print((r,c))
			visited.append((r, c))
			if m[r][c] == 0:
				all_r.append(r)
				all_c.append(c)
			for newr, newc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
				if isValid(m, newr , newc):
					q.insert(0, (newr, newc))
	print(all_c)
	print(all_r)
	return [max(all_c)-min(all_c)+1, max(all_r)-min(all_r)+1]
            

matrix = [[1,1,1,1,1,1],
		  [1,1,1,1,1,1],
		  [1,1,1,0,0,0],
		  [1,1,1,0,0,0],
		  [1,1,1,0,0,0]
		 ]
#3, 3
print(findSubmatrix(matrix))





# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     matrix_rows = int(input().strip())
#     matrix_columns = int(input().strip())

#     matrix = []

#     for _ in range(matrix_rows):
#         matrix.append(list(map(int, input().rstrip().split())))

#     result = findSubmatrix(matrix)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
