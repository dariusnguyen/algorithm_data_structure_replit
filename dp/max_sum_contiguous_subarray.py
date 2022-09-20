'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
'''
'''
Dynamic programming/Kadane's algorithm solution:
local maximum[i] = max(arr[i], arr[i] + local_maximum[i-1])
Time: O(n)
'''

def max_sum_subarray(nums):
	global_max = float('-inf') #init global max to negative infinity
	local_max = 0
	for i in range(len(nums)):
		local_max = max(nums[i], nums[i] + local_max)
		global_max = max(local_max, global_max)
	return global_max