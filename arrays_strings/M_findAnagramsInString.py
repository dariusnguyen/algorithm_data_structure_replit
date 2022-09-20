'''
438. Find All Anagrams in a String
Medium

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
'''

'''
Idea: use sliding window, create a "rolling" hash map of the current window in string s. Compare it with p's hashmap
Reason: all anagrams of p have the same hash map of character --> count
Time: O(n) where n is len(s). n>m where m is len(p)
Space: O(m)
'''

def findAnagrams(s, p):
	pMap = {}
	for i in p:
		pMap[i] = pMap.get(i, 0) + 1

	windowMap = {}
	l = 0
	r = 0
	res = []
	while r < len(s):
		#add the current right char first
		windowMap[s[r]] = windowMap.get(s[r], 0) + 1
		
		#if the current window has sufficient length. initially, this block will be skipped to populate the empty hash map
		if (r - l) == len(p)-1:
			#check if the current window is a match
			if windowMap == pMap:
				res.append(l)
			#remove the current left char and slide left pointer
			windowMap[s[l]] -= 1
			if windowMap[s[l]] == 0:
				windowMap.pop(s[l])
			#slide left pointer
			l += 1

		#slide right pointer
		r += 1

	return None if res == [] else res

	
#    0123456789
s = "cbaebabacd"
p = "abc"

print(findAnagrams(s,p))

s1 = "abab"
p1 = "ab"
print(findAnagrams(s1,p1))

'''
len p =4
01234
sfsafasfa
l
    r
'''