'''
347. Top K Frequent Elements
Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

'''
Method 1: use a hash table and a heap

loop through the array and build a dict
	key: number
	value: count
create a heap, then push the first k items from the dict
for each remaining item in the dict, push then pop immediately to maintain size k
the final heap will contain the top k frequent items
'''
import heapq
def topKFrequentElements(nums, k):
	freq = {}
	for i in nums:
		freq[i] = freq.get(i, 0) + 1

	print(freq)
	freq = [(v,k) for k, v in freq.items()]
	heap = []
	heapq.heapify(heap)
	for i in range(len(freq)):
		heapq.heappush(heap, freq[i])
		if i>k-1:
			heapq.heappop(heap)
	'''
 	Note: a slighly more optimized way is to separate the first k iterations from the remaining
  	and use heapq.heappushpop() since it is more efficient than heappush() and heappop() separately
 	'''
	return [i[1] for i in list(heap)]

nums = [5,6,1,1,4,3,8,4,0,0,4,6,8,8,9,10,9,3,5,0,1]
k = 3
print(topKFrequentElements(nums, k))
