'''
392. Is Subsequence
Easy

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 
Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

'''

'''
Method 1: 2 pointers sP and tP

while sP<len S and tP < len P
	if s[sP] == t[tP]:
 		increment sP and tP
   	else
		increment tP

if tS < len S
	return False
 else return true

Time: O(m) where m = len(t)
Space: O(1)
'''

def isSubsequence_2pointers(s, t):
	sP = tP = 0
	while sP < len(s) and tP < len(t):
		if s[sP] == t[tP]:
			sP += 1
		tP += 1
	if sP < len(s):
		return False
	return True

'''
Method 2: Divide and conquer with greedy and recursion

recurse(s, t)
base case 0: if len(s) == 0 ( we have found matches for all chars in s)
				return True
base case 1: if len(t) == 0 (we have exhausted all of t but didn't find a match)
				return False
recursive case 0: if s[0] == t[0]
				recurse(s[1:], t[1:])
(greedily use the first match we find for the current character, although there might be others)
recursive case 1: if s[0] != t[0]
				recurse(s, t[1:])

Time: O(m)
Space: O(m)
'''

def isSubsequence_recursive(s, t):
	# print('s:', s, 't:', t)
	if len(s) == 0:
		return True
		
	if len(t) == 0:
		return False
		
	if s[0] == t[0]:
		return isSubsequence_recursive(s[1:], t[1:])
		
	return isSubsequence_recursive(s, t[1:])

'''
Method 3: Greedy with hashmap & binary search
This method optimizes for repeated calls of the function where we have different source strings s0, s1, s2... but only 1 target string t

class isSubsequence
build a hash map from t
	char --> list of indices in t

use a var to track current position in t
loop through s
	lookup char i of s in the hash map
		since the indices are already sorted,
 		use binary search to search for the first matching index of t greater than the current index
   			if the search doesn't find a result, then we have exhausted t
	  			return False
return True
'''

class isSubsequence:
	def __init__(self, t):
		self.chars = {}	
		for i in range(len(t)):
			if i in self.chars:
				self.chars[t[i]].append(i)
			else:
				self.chars[t[i]] = [i]
		
	def isSubsequence(self, s):
		currIndex = 0
		for i in s:
			if i not in self.chars:
				return False
			res = self.binarySearch(currIndex, self.chars[i])
			# print(f'i={i} search({currIndex}, {self.chars[i]})={res}')
			if res is None:
				return False
			else:
				currIndex = res
		return True

	def binarySearch(self, target, nums):
		'''
	 	search for immediate value >= target
		[0 2 4 5 8]
		3
		left = 0
		right = len nums
	 	while left <= right:
		if val at mid >= target
	 		right = mid - 1
	   	else
			left = mid + 1
	    return left
	 	'''
		l = 0
		r = len(nums) - 1

		while l <= r:
			m = l + (r - l) //2
			if nums[m] >= target:
				r = m - 1
			else:
				l = m + 1
				
		if l >= len(nums):
			return None
		return nums[l]

	


s0 = 'axc'
t0 = 'ahbgdc'
#False

s1 = 'axc'
t1 = 'axc'
#True

s2 = 'axc'
t2 = 'ax'
#False

s3 = 'ace'
t3 = 'abcde'
#True

s4 = 'aec'
t4 = 'abcde'
#False

s5 = 'n'
t5 = 'abcde'
#False


# for s, t in [(s0, t0), (s1, t1), (s2,t2), (s3, t3), (s4,t4), (s5,t5)]:
# 	print(isSubsequence_recursive(s,t))

t = 'abcde'
check_t = isSubsequence(t)

for s in [s0, s1, s2, s3, s4, s5]:
	print(check_t.isSubsequence(s))

