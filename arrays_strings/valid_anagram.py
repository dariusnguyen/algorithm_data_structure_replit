'''
https://leetcode.com/problems/valid-anagram/

242. Valid Anagram
Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''

'''
create a function to create a dict of character counts in a string
def get_count_dict(s):
  create empty c_dict
  for each char in string:
    if char is in dict, increment count
    else add char to dict with count 1
a = get_count_dict(s)
b = get_count_dict(t)
if a==b, return true
else return false

Time: O(n+m)
Memory: O(n+m)

Corner cases:
- strings don't have the same length: check lens first
- strings have different cases: convert both to lower case
- one or both strings are empty: return False
'''

def is_anagram(s: str, t: str) -> bool:
  if len(s) != len(t) or len(s)==0 or len(t)==0:
    return False

  s = str.lower(s)
  t = str.lower(t)
    
  def get_count_dict(s):
    c_dict = {}
    for c in s:
      if c_dict.get(c) is None:
        c_dict[c] = 1
      else:
        c_dict[c] += 1
    return c_dict

  a = get_count_dict(s)
  b = get_count_dict(t)
  return a==b