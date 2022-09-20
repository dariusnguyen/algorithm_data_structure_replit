'''
238. Product of Array Except Self
Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

'''
'''
Method 1:
Idea: The product except self of element i is basically the product of its prefix product and suffix product. We can traverse the array to calculate the prefix product and suffix arrays, then use them to calculate the answer array

time: O(n)
space: O(n)
'''

def product_except_self_1(nums):
	n = len(nums)
	prefix = [1]
	for i in range(1, n):
		prefix.append(nums[i-1] * prefix[i-1])

	suffix = [1] * n
	for i in range(n-2, -1, -1):
		suffix[i] = nums[i+1] * suffix[i+1]
	
	res = [prefix[i] * suffix[i] for i in range(n)]

	return res

'''
Method 2:
Idea is the same as method 1, but avoid creating separate prefix and suffix arrays to save space
time: O(n)
space: O(1)
'''

def product_except_self_2(nums):
	n = len(nums)

	res = [1]
	for i in range(1, n):
		res.append(res[i-1] * nums[i-1])

	suffix = 1
	for i in range(n-1, -1, -1):
		res[i] = res[i] * suffix
		suffix = suffix * nums[i]
		
	return res
	
'''
Another way to implement method 2
'''
def compute(arr):
	n = len(arr)
	
	i, temp = 1, 1

	prod = [1 for i in range(n)]
	
	for i in range(n):
		prod[i] = temp
		temp *= arr[i]
	print(prod)

	temp = 1

	for i in range(n-1, -1, -1):
		prod[i] *= temp
		temp *= arr[i]

	return prod