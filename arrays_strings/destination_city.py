'''
Destination City
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

Example 1:

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:

Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

Example 3:

Input: paths = [["A","Z"]]
Output: "Z"
'''
'''
U
	Q's:
		Can paths be an empty list?
		What if paths[i] doesn't follow [cityAi, cityBi]?

	Assumptions:
		paths is a valid list with the format specified

	Edge cases:
		paths has 1 element only

M
	array + dict
P
	create a dict store counts
	loop through paths
	for each pair Ai, Bi
		if Ai is not in dict:
			add Ai as key, 1 as value
		if Ai is in dict:
			increment count by 1
		add Bi as key, 0 as value
	look for key where value is 0
	return that element

	time: O(n) where n = len(paths)
	space: O(n) in worst case (many different cities)

I
R
E

'''

def get_destination(paths):
	counts = {}
	for path in paths:
		#if city Bi exists, increment its count by 1. If it doesn't exist, create an entry with value 1
		counts[path[0]] = counts.get(path[0], 0) + 1	
		
		#if city Bi exists, leave value as is. If it doesn't exist, create an entry with value 0
		counts[path[1]] = counts.get(path[1], 0)
	print(counts)
	for a, count in counts.items():
		if count == 0:
			return a
			