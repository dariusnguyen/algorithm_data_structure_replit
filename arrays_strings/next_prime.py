'''
Given a number, return the next smallest prime number

Note: A prime number is greater than one and has no other factors other than 1 and itself.

Examples:
Input: 3
Output: 5

-----------------
UMPIRE

U
	questions: what if input is a negative number? return 2, since 2 is the smallest prime
				is there a guaranteed solution? yes
	edge cases: n<=1: return 2
				n<=2: return 3 (special case since sqrt(3)<2)
				n is not an int: start from ceil(n)
M
	use math knowledge
P
	pseudo code:
	loop through numbers greater than input
	for each number i
		perform primality test by loop through 2 to sqrt(i)
			if i is divisible by any number in that range, it is not a prime
			after looping through all in that range, if cannot find a factor, then return number i

	time: let m be the next prime after n. O( (m-n)*sqrt(m) ) = O( sqrt(m) )
	space: O(1)

I
'''
# import math
def next_prime(n):
	if n<=2:
		return 2
	if n<3:
		return 3
	i = int(n) + 1
	while True:
		flag = False
		for j in range(2, int(i**(1/2))+1):
			if i%j==0:
				flag = True
				break
		if flag == True:
			i+=1
		else:
			return i