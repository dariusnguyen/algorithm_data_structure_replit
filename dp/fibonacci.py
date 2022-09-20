'''
Implement a function to calculate the n-th fibonacci number using dynamic programming

init a dict for memoization
recursive function:
	if i in dict:
		return fib(i)
	base case:
	if i==0:
		return 0
	if i==1:
		return 1

	calculate fib(n-1) + fib(n-2)
	store it in dict
	return it
'''

def fib_dp(n, mem = {}):
	if n==0:
		return 0
	if n==1:
		return 1
	if mem.get(n):
		return mem[n]

	mem[n] = fib_dp(n-1, mem) + fib_dp(n-2, mem)
	return mem[n]

