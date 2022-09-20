'''
349. Intersection of Two Arrays
Easy

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

'''
'''
UMPIRE
U
	assumptions: arrays are not sorted, contains only integers
M
	set?
P
	s1 = set(nums1)
	s2 = set(nums2)
	result = s1.intersection(y)
	
	time: O(m + n + min(m,n))

	create a dict for each value in nums1 as a key
		by looping
	loop through nums2
		if num i in nums 2 is in dict
			add to return list

	time: O(m+n)
	
I
	
R
E
'''

def intersection(nums1, nums2):
	d1 = {}
	res = set()
	for i in nums1:
		d1[i] = d1.get(i, 0) + 1
	for i in nums2:
		if d1.get(i,0) != 0:
			res.add(i)
			
	return res
