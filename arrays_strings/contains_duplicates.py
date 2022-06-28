'''
https://leetcode.com/problems/contains-duplicate/
217. Contains Duplicate
Easy

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

'''
create nums_dict empty dictionary
for each num in list:
  if num is in nums_dict:
    return true
  else:
    add num to nums_dict
return false

Time complexity:
  Best case: O(1)
  Worst case: O(n)
Mem complexity:
  Best case: O(1)
  Worst case: O(n)
'''
def contains_duplicates(nums):
  nums_dict = {}
  for i in nums:
    if nums_dict.get(i) is not None:
      return True
    else:
      nums_dict[i] = 1
  return False