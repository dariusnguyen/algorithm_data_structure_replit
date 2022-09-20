'''
(same as https://leetcode.com/problems/unique-paths/)

We have an m by n grid an a "traveller" stands in the top left cell. The traveller can only move down or right. Write a function to calculate the number of unique ways the traveller can travel to the bottom right cell.

U
	Q's: Restrictions for m and n?
		m, n >=1
	
M
	DP
P
	after each move, the grid gets smaller => smaller subproblem
	init dict for memoization
	base case: if m or n < 0, then it's an invalid grid, return 0
	base case: if grid(m,n) in dict, return stored value
	base case: if m==n==1, return 1
I
R
E

'''

def count_ways(m, n, mem={}):
	if m<1 or n<1:
		return 0
	if m==1 and n==1:
		return 1
	if mem.get((m,n)):
		return mem[(m,n)]
	mem[(m,n)] = count_ways(m-1, n, mem) + count_ways(m, n-1, mem)
	return mem[(m,n)]

