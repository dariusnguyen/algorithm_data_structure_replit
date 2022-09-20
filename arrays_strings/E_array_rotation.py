'''
Given a 2D array, rotate it in the clockwise direction
[[1,2,3],[4,5,6],[7,8,9]]
[[7,4,1][8,5,2][9,6,3]]

1 2  3  4
5 6  7  8
9 10 11 12

9  5  1
10 6  2
11 7  3
12 8  4
time: O(n)
space: O(n)
'''

def rotateArray(arr):
	m = len(arr)
	n = len(arr[0])
	
	newarr = [[] for i in range(n)]
	for i in range(m):
		for j in range(n):
			newarr[j].insert(0, arr[i][j])

	return newarr

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(rotateArray(arr))