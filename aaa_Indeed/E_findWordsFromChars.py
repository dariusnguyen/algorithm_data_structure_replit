'''
1160. Find Words That Can Be Formed by Characters
Easy

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
'''

'''
atach
words = cat bt hat tree
cat hat 

welldonehoneyr

hello world leetcode
hello world lee


create a dict from string
key: char
value: count

for each word
create a dict
for each key, if dict from string has equal or higher count then word is good
add num chars to total

time: O(m+n) where m = total num chars in words, n = num chars in string
space: O(1) since there is a constant number of characters (26)
'''

def countCharacters(self, words: List[str], chars: str) -> int:
	stringDict = {}
	for c in chars:
		stringDict[c] = stringDict.get(c, 0) + 1
	
	res = 0
	for word in words:
		wordDict = {}
		for c in word:
			wordDict[c] = wordDict.get(c, 0) + 1
			
		isGood = True
		for k, v in wordDict.items():
			if stringDict.get(k) is None or stringDict[k] < v:
				isGood = False
				break
		if isGood:
			res += len(word)
	return res