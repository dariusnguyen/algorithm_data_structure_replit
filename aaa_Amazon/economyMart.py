from heapq import heappush, heappop, heapify

'''
heap = []
heapify(heap)

heappush(heap, (4, 'fries'))
heappush(heap, (2, 'soda'))
print(len(heap))
print(heappop(heap))
print(heappop(heap))
# print(heap[0])
# print(heap[1])
heappush(heap, (5, 'hamburger'))
print(heappop(heap))
# print(heap[2])
heappush(heap, (4, 'nuggets'))
heappush(heap, (1, 'cookies'))
print(heappop(heap))
# print(heap[3])
'''
'''
max heap of size k
top of max heap is the kth cheapest
insert into max heap
'''

class DB:
	def __init__(self):
		self.minHeap = []
		self.maxHeap = []
		self.i = 1

	def insert(self, name, price):
		


