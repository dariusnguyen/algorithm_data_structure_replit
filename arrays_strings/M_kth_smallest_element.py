'''
Given an array and a number k where k is less than size of array, we need to find the k’th smallest element in the given array. It is given that all array elements are distinct.

Examples:

Input: [7, 10, 4, 3, 20, 15]  --> [3 4 7 10 15 20]
       k = 3
Output: 7

Input: [7, 10, 4, 3, 20, 15] --> [3 4 7 10 15 20]
       k = 4
Output: 10
'''

'''
Method 1: Brute force:
perform sorting
return the kth element of the sorted array
time: O(nlogn)
space: O(1)

Method 2:
modified quick sort
recurse(arr, first, last)
	pick pivot index: last element
	partition the subarry bw first and before last
	if left index == k
		return k
	else
		recurse(arr, first, pivot index - 1)
		recurse(arr, pivot index, last)

partition(arr, l, r):
	if len(arr)<=1:
		return arr
	while True:
		while arr[l] < arr[p]:
			l+=1
		while arr[r] >= arr[p]:
			r-=1
		if l>=r
			break

		else
			swap arr[l], arr[r]
			l+=1
			r+=1

time: worst case is when k == n and pivot is always the largest or smallest (when array is already sorted)
		O(n^2)
space: worst case we have to recurse n times, so O(n)
		
'''

def partition(arr, l, r, p = None):
	if p is None:
		p = r
		r -= 1

	# print(f'l,r,p ={l, r, p}')
	if len(arr) > 1:
		while True:
			while arr[l] < arr[p]:
				l += 1
			# print(f'arr[r] = {arr[r]}')
			
			while arr[r] > arr[p]:
				r -= 1
				# print(f'r = {r}')
			if l >= r:
				break
			else:
				arr[l], arr[r] = arr[r], arr[l]
				l += 1
				r -= 1
		arr[l], arr[p] = arr[p], arr[l]
	return l


def kth_smallest(arr, k):
	# l = 0
	# r = len(arr) - 1
	k -= 1 #convert 1-indexing to 0-indexing

	def recurse(arr, l, r):
		if l==r: #when there is only 1 element left in the subarray, it must be the one we're looking for
			return arr[l]
		else: #when there are more than 1 element in the subarray
			sortedIndex = partition(arr, l, r)
			nonlocal k			
			if sortedIndex == k:
				return arr[k]
			elif sortedIndex < k:
				return recurse(arr, sortedIndex + 1, r)
			else:
				return recurse(arr, l, sortedIndex - 1)
	
	return recurse(arr, 0, len(arr)-1)
			
			
	



arr = [7, 10, 4, 3, 20, 15] #--> [3 4 7 10 15 20]
# print(partition(arr, 0, len(arr)-1))
print(kth_smallest(arr, 4))
	

