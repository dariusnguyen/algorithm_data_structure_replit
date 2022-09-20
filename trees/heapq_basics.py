import heapq

nums = [5,2,1,6,9,6,1,3,4,20]

#convert the list to a min heap
heapq.heapify(nums)
print(list(nums))

#peek at the root--smallest item
print(nums[0])

#pop the root
print(heapq.heappop(nums))

#push a new item
heapq.heappush(nums, 0)
print(list(nums))

#retrieve the n largest items
n = 5
print(heapq.nlargest(n, nums))

#retrieve the n smallest items
print(heapq.nsmallest(n, nums))
