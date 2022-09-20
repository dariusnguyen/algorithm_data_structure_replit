'''
278. First Bad Version
Easy

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.


Example 2:

Input: n = 1, bad = 1
Output: 1

Constraints:

1 <= bad <= n <= 231 - 1

'''

'''
n = 5
bad = 4
[g g g b b]
 1 2 3 4 5

n=2
b=2
[g b]

edge case:

n=1
b=1
[b]

[g g ... g b]

mid = (f + l) / 2
check mid
if mid

[ g b b   b    ]
    .  .  .  

time: O(logn)
space: O(logn) or O(1)
'''
def isBadVersion(i):
	pass
def firstBadVersion(n):
	rightmostGood = -1
	leftmostBad = -1
	l = 1
	r = n
	while rightmostGood + 1 != leftmostBad:
		mid = r + (l - r)//2
		if isBadVersion(mid):
			leftmostBad = mid
			r = mid - 1
		else:
			rightmostGood = mid
			l = mid + 1

	return leftmostBad

'''
[g g g b b]
[1 2 g 4 5]

mid = 4 + (5-4)//2 = 4
isBadVersion(mid) = True
leftmostBad = 4
r = 4 - 1 = 3

rightmostGood = 3 + 1 = leftmostBad = 4
stop

return 4

'''