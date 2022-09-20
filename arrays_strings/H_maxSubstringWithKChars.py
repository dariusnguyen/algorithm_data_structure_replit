'''
Longest Substring with k distinct characters
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Examples:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Input: String="cbbebi", K=3
Output: 5
'''

'''
araaci

2 pointers start at 0
init maxlen
init dict of chars and counts
while num distinct chars < k
	increment right pointer
	if num distinct == k
		compare and update maxlen

		update dict with new count of char at left pointer
		increment left pointer
	else if num distinct < k:
		increment right pointer
		add or increment count of char at right pointer to dict
	if num distinct > k:
		update dict with new count of char at left pointer
		increment left pointer
		

return maxlen
'''

def maxSubstringKChars(s, k):
	print(f'k={k}')
	l = r = 0
	chars = {}
	# chars[s[0]] = 1
	maxLen = 0
	maxString = ''
	while r < len(s):
		substr = s[l:r]
		print()
		print(f'current substr:"{substr}"')
		if len(substr) > maxLen:
			maxString = substr
		maxLen = max(maxLen, len(substr))
		print(chars, f'r= {r} maxLen= {maxLen} maxString= {maxString}')
		
		if len(chars) <= k:
			print(f'lenchars={len(chars)} <= k={k} --> add')
			# if r==len(s):
			# 	break
			r += 1
			chars[s[r-1]] = chars.get(s[r-1], 0) + 1
			# chars[s[l]] -= 1
			# if chars[s[l]] == 0:
			# 	chars.pop(s[l])
			# l += 1
		# elif len(chars) < k:
		# 	r += 1
		# 	chars[s[r]] = chars.get(s[r], 0) + 1
		else: #len(chars)>k
			print(f'lenchars= {len(chars)} > k= {k} --> remove')
			chars[s[l]] -= 1
			if chars[s[l]] == 0:
				chars.pop(s[l])
			l += 1
			# print(chars)
			

				

	return maxLen, maxString