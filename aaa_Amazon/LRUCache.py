'''
146. LRU Cache
Medium

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.

int get(int key) Return the value of the key if the key exists, otherwise return -1.

void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); # cache is {1=1}
lRUCache.put(2, 2); # cache is {1=1, 2=2}
lRUCache.get(1);    # return 1
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    # returns -1 (not found)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    # return -1 (not found)
lRUCache.get(3);    # return 3
lRUCache.get(4);    # return 4
'''

'''
use a dict key: value
use a linkedlist to store get frequency
use dict2 key: Node
when get() is called, move key to next node
when put() is called and cache is full, evict one key from head node
'''

class Node:
	def __init__(self, count, next):
		self.count = count
		self.keys = set()
		self.next = next

class LRUCache:
	def __init__(self, maxSize):
		self.maxSize = maxSize
		self.dict1 = {}
		self.dict2 = {}
		self.head = Node(0, None)

	def put(self, key, value):
		if key in self.dict1:
			self.dict1[key] = value
		else:
			if len(self.dict1) == self.maxSize:				
				evictKey = self.head.keys.pop()
				self.dict1.pop(evictKey)
				self.dict2.pop(evictKey)
							
			self.dict1[key] = value
			self.dict2[key] = self.head
			self.head.keys.add(key)

	def get(self, key):
		if key in self.dict1:
			node = self.dict2[key]
			print('key', key)
			print(node.keys)
			node.keys.remove(key)
			if node.next is None:
				node.next = Node(node.count+1, None)
			node.next.keys.add(key)
			return self.dict1[key]

		else:
			return -1
			
		
lRUCache = LRUCache(2)
lRUCache.put(1, 1); # cache is {1=1}

lRUCache.put(2, 2); # cache is {1=1, 2=2}
# print(lRUCache.dict1)
# print(lRUCache.dict2[1].keys)
lRUCache.get(1);    # return 1
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    # returns -1 (not found)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    # return -1 (not found)
lRUCache.get(3);    # return 3
lRUCache.get(4);    # return 4				
		
			
			

		
