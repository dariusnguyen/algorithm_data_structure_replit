'''
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.

inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.

dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.

getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".

getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".

Note that each function must run in O(1) average time complexity.

Example:

AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("goodbye");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "goodbye"

'''

# class AllOne(object):

#   def __init__(self):
#     self.head = Node(0, None, None)
#     self.tail = Node(0, None, None)
#     self.head.after = self.tail
#     self.tail.before = self.head
#     self.dict = {}

#   def inc(self, key):
#     """
#     :type key: str
#     :rtype: None
#     """
#     if key not in self.dict:
#       self.head.after.keys.add(key)
#     else:
#       node = self.dict[key]
#       node.keys.remove(key)
      
#       nextnode = node.after
#       nextnode.keys.add(key)


#   def dec(self, key):
#     """
#     :type key: str
#     :rtype: None
#     """
#     self.dict[key] -= 1

#   def getMaxKey(self):
#     """
#     :rtype: str
#     """
#     return self.tail.before.keys.pop()
  

#   def getMinKey(self):
#     """
#     :rtype: str
#     """
#     return self.head.after.keys.pop()
        
# class Node():
#   def __init__(self, count, before, after):
#     self.keys = set()
#     self.before = before
#     self.after = after
#     self.count = count

class Node():
	def __init__(self, count, prev, next):
		self.count = count
		self.prev = prev
		self.next = next
		self.keys = set()

class AllOne():
	def __init__(self):
		self.dummyHead = Node(0, None, None)
		self.dummyTail = Node(0, None, None)
		self.dummyHead.next = self.dummyTail
		self.dummyTail.prev = self.dummyHead
		
		self.dict = {}

	def inc(self, key):
		if key in self.dict:
			node = self.dict[key]
			node.keys.remove(key)

			if node.next is None:
				node.next = Node(node.count+1, node, None)
			node.next.keys.add(key)

		else:
			dict[key] = self.dummyHead.next
			self.dummyHead.next.keys.add(key)

	def dec(self, key):
		assert key in self.dict #assume the key already exists
		node = self.dict[key]
		node.keys.remove(key)
		node.prev.keys.add(key)

	def getMaxKey(self):
		node = self.dummyTail.prev
		return node.keys.pop()

	def getMinKey(self):
		node = self.dummyHead.next
		return node.keys.pop()
		

'''

{
	hello: Node(2, {hello})
	goodbye: Node(1, {goodbye})
}


0  1   2   3   4   5   6
N()
'''

# Your AllOne object will be instantiated and called as such:
# allOne = AllOne()
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.inc("goodbye");
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()


class AllOne2():
	def __init__(self):
		self.dict = {}
		self.max = 0
		self.min = 0
		self.maxKey = ''
		self.minKey = ''

	def inc(self, key):
		count = self.dict.get(key, 0) + 1
		self.dict[key] = count
		if count > self.max:
			self.maxKey = key

	def dec(self, key):
		self.dict[key] -= 1
		count = self.dict[key]
		if count == 0:
			self.dict.pop(key)
		else:
			if count < self.min:
				self.minKey = key

	def getMaxKey(self):
		return self.maxKey

	def getMinKey(self):
		return self.minKey
		
		
		