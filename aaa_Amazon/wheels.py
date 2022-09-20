'''
There are 2 types of vehicles: 2-wheel and 4-wheel

Given a list 'arr' of required number of wheels, return a list of the number of possible unique combinations of vehicles.

Example:
Input: arr = [4,5,6]
Output: [2, 0, 2]

Explanation: To get a total of 4 wheels, there are 2 ways:
				2 x 2-wheel vehicles
				1 x 4-wheel vehicle
			To get a total of 5 wheels, there are 0 possible ways.
   			To get a total of 6 wheels, there are 2 ways:
				3 x 2-wheel vehicles
				1 x 4-wheel vehicle + 1 x 2-wheel vehicle

Match: count all possible ways --> backtracking

Approach:
backtracking using recursion
recurse(target, startIndex)
	if target = 0
 		good combination -> return 1 to add to count
   if target < 0:
   		abandon -> return 0 to add to count
	else
 	init count
  	loop through candidates from startIndex
 		count += recurse(target - candidate i, startIndex = i)
	return count
'''

def chooseFleet(arr):
	res = []
	candidates = [2,4]

	def recurse(target, startIndex):
		if target == 0:
			return 1
		if target < 0:
			return 0
		count = 0
		for i in range(startIndex, len(candidates)):
			count += recurse(target - candidates[i], i)
		return count

	for i in arr:
		if i % 2 != 0:
			res.append(0)
		else:
			res.append(recurse(i, 0))
	return res

arr = [4, 5, 6, 7, 8]
print(chooseFleet(arr))