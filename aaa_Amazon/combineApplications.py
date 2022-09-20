'''
Given 2 lists of pairs of integers:
1. Foreground applications, where each pair consists of a foreground app ID and its memory requirement
2. Background applications, where each pair consists of a background app ID and its memory requiremen

and an integer representing a device's memory capacity

Find the most optimal pair of foreground and background applications for that device. The pair is consider most optimal if there is no other pair that uses more memory than this pair, yet consume no more memory than the device's capacity.

Example:
foregroundAppList = [[1,2], [2,4], [3,6]]
backgroundAppList = [[1,2]]
deviceCapacity = 7

output: [[2,1]]
explanation: foreground [2,4] and background [1,2] makes the best pair since they use the most memory of 4+2 = 6

'''

'''
explore every possible combination of foreground and background
record the one with minimum & positive remaining memory

time: O(n*m)
space: O(1)
'''

def combineApplications(foreground, background, cap):
	res = None
	maxMem = None
	first = True
	
	for i in foreground:
		for j in background:
			fID, fMem = i[0], i[1]
			bID, bMem = j[0], j[1]

			if first or (fMem + bMem < 7 and maxMem < fMem + bMem):
				res = [fID, bID]
				maxMem = fMem + bMem
				first = False
	return res

foregroundAppList = [[1,2], [2,4], [3,6]]
backgroundAppList = [[1,2]]
deviceCapacity = 7

print(combineApplications(foregroundAppList, backgroundAppList, deviceCapacity))