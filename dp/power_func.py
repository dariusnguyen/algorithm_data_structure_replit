'''
Problem #3 Pow(x,n)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Examples:

Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25


UMPIRE

U
	Questions: Any constraints on x and n? assume any integer.
	Edge cases: x = 1: return 1
				n = 0: return 1
				n < 0: return 1/x^n
				

M
	recursion
P
	## Method1
	base case: x = 1: return 1
				n = 0: return 1
				n<0: return 1/pow(x, n)
	recursive step: return x * pow(x, n-1)

	time: O(n)
	space: O(1)

	## Method 2 (optimal)
	idea:
		let k = n//2
		if n even:
			x^n = (x^k)^2
		if n odd:
			x^n = (x^k)^2 * x
	time: O(log(n))
	space: O(1)
I
'''

# Method 1
# def pow(x:int, n:int):
# 	if x==1:
# 		return 1
# 	if n==0:
# 		return 1
# 	if n<0:
# 		return 1/pow(x, -n)
# 	return x * pow(x, n-1)

# Method 2

def pow(x:int, n:int):
	if x==1:
		return 1
	if n==0:
		return 1
	if n==-1:
		return 1/x
	k = n//2
	return pow(x, k)**2 * (x if n%2 else 1)

'''
R

E

'''