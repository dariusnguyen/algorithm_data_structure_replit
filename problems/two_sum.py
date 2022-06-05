'''
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

'''
UMPIRE
U
Can there be multiple pairs? No
Can a num be reused? No
Empty list or list of length 1? Return empty list
List can contain negative numbers? Yes
If no pairs add up to target, return empty list? Yes
Corner case: repeated numbers that add up to the target. Ex: 3+3=6
M
use dict to store indexes

P
init empty res list
init empty dict
loop through the nums list
for each num x in list
  if x in dict:
    continue #assume single solution
  else:
    add x:x_index to dict
  
for each key x in dict
  y = target - x
  query dict for y
  if y is found:
    add x and y's index to list
    return

return res list

Time: O(n)
Space:
  Best case: O(1) #repeated nums
  Worst case: O(n) #all unique
'''
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
	res = []
	if len(nums)>1:
		nums_idx = {}
		for i, x in enumerate(nums):
			if nums_idx.get(x) is not None:
				nums_idx[x].append(i)
			else:
				nums_idx[x] = [i]

	for x, x_idx in nums_idx.items():
		y = target - x
		if y == x:
			if len(x_idx)>1:
				res.append(x_idx[0])
				res.append(x_idx[1])
				return res
			else:
				continue
		y_idx = nums_idx.get(y)
		if y_idx is not None:
			res.append(nums_idx[x][0])
			res.append(y_idx[0])
			return res
	return res

'''
Review

Evaluate
'''