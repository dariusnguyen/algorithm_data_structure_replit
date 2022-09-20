'''
22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
'''

'''
build the string using recursion
only continue to recurse if it is valid (backtracking)

use openRemain and closeRemain to track remaining open and close parens
consider 2 potential candidates: ( and )
if openRemain == 0 and closeRemain == 0
	append string to result
if openRemain > 0
	append ( and recurse
if closeRemain<=openRemain
	append ) and recurse

((
openR = 1
closeR = 3
'''

def generateParentheses(n):
	def recurse(s, openRemain, closeRemain):
		if openRemain == 0 and closeRemain == 0:
			res.append(s)
			return
		if openRemain > 0:
			recurse(s + '(', openRemain-1, closeRemain)
		if closeRemain > openRemain:
			recurse(s + ')', openRemain, closeRemain-1)

	res = []
	recurse('', n, n)
	return res	

print(generateParentheses(1))