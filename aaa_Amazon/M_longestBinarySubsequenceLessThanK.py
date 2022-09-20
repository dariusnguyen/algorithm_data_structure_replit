'''
2311. Longest Binary Subsequence Less Than or Equal to K
Medium

You are given a binary string s and a positive integer k.

Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

Note:

The subsequence can contain leading zeroes.
The empty string is considered to be equal to 0.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
 

Example 1:

Input: s = "1001010", k = 5
Output: 5
Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.

Example 2:

Input: s = "00101001", k = 1
Output: 6
Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
The length of this subsequence is 6, so 6 is returned.
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.
1 <= k <= 109

            0123456
			6543210
Input: s = "1001010", k = 5
             00.010

Input: s = "00101001", k = 1
			00.0.001

'''

'''
loop through the string
	count zeros
	gather list of indices of 1
loop through list of 1's
	for each index
 		new number = num + 2**(index)
 		if new number<k
   			increment count
	  	else
			return count
time: O(n)
space: O(n)
'''

def longestBinarySubsequence(s, k):
	n = len(s)
	count = 0
	stack = []
	for i in range(n):
		if s[i] == '0':
			count += 1
		else:
			stack.append(n-i-1)
	num = 0
	# print('0 count:', count)
	while stack:
		i = stack.pop()
		num += 2**i
		if num > k:
			return count
		else:
			count += 1
	return count

s0 = '1001010'
k0 = 5

s1 = '00101001'
k1 = 1

for s, k in [(s0, k0), (s1, k1)]:
	print(longestBinarySubsequence(s, k))