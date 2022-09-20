'''
Hackerrank Assessment

The number of goals of 2 teams are given in the form of 2 lists. For each score of team B, return the number of matches where team A scores less than or equal to team B.

Example:
teamA = [1, 2, 3]
teamB = [2, 4]
output = [2, 3]
Explanation: In team B's first match, they scored 2 goals. Team A has 2 matches where they scored less than or equal to 2 goals. In team B's second match, they scored 4 goals. Team A has 3 matches where they scored less than or equal to 4 goals. 

'''

'''
sort team A
for each score of team B, perform binary search in team A for the first index strictly greater than the curr team B's score
since the score of team B can be greater than all of team A's scores, the starting range of binary search should be [0, len(A)], inclusive of index len(A) which is after the last index
'''

def binarySearch(target, arr):
	l = 0
	r = len(arr)
	while l<r:
		mid = l + (r-l)//2
		if arr[mid] > target: #move left
			r = mid
		else: #move right
			l = mid + 1
	return r
arr = [2,2,3,5,5,7,7]	

# assert(binarySearch(0, arr)==0) #0 scores <= 0
# assert(binarySearch(2, arr)==2) #2 scores <= 2
# assert(binarySearch(7, arr)==7) #7 scores <= 7
# assert(binarySearch(8, arr)==7) #7 scores <= 8

def binarySearch2(target, arr):
	l = 0
	r = len(arr)-1
	while l<=r:
		mid = l + (r-l)//2
		if arr[mid] > target: #move left
			r = mid - 1
		else: #move right
			l = mid + 1
	return l

assert(binarySearch2(0, arr)==0) #0 scores <= 0
assert(binarySearch2(2, arr)==2) #2 scores <= 2
assert(binarySearch2(7, arr)==7) #7 scores <= 7
assert(binarySearch2(8, arr)==7) #7 scores <= 8