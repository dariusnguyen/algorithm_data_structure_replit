'''
Given an unsorted array of integers, we want to find the length of the longest subsequence such that elements in the subsequence are consecutive integers. The consecutive numbers can be in any order.

Examples:

Input: [1, 9, 3, 10, 4, 20 , 2]
Output: 4
[1, 3, 4, 2] is the longest subsequence of consecutive elements.
'''

'''
UMPIRE

* U
Edge cases:
	Empty array
		assume: return None
	Array of 1 int
		assume: return None (or 1?)
	No consecutive integers in the array
		assume: return None (or 1?)

* M
Array + Hash map/dictionary

* P
Method 1:
create a dict to store numbers exist in the array
loop through numbers in array
	if number i doesn't exist, add it
get list of keys of the dict
sort keys (?)
init max
init counter
loop through keys
	if key i is the same as previous key
		continue
	if key i == key i-1
		counter +=1
	else
		max = counter
		counter = 0

return max

Time: O(n + nlogn) = O(nlogn)
Space: O(n)

Method 2: Optimal solution
create a set of unique nums from the original array
init max = 0
loop through the set
	if (num i) - 1 exists in the set
		continue #because it's not the first number in a sequence
	else
		init counter = 1
		while loop until num i + 1 is not found
			increment counter
		if counter > max
			max = counter
return max

Time: O(n)
Space: O(n)
'''

# Method 2: optimal
from typing import List
def max_length_consecutive(nums: List[int]):
	nums_set = set(nums)
	max_len = 0
	for i in nums_set:
		if i-1 in nums_set:
			continue
		else:
			j=i
			counter = 1
			while j+1 in nums_set:
				counter += 1
				j+=1
			max_len = max(counter, max_len)

	print('set: ', nums_set)
	return max_len
			
