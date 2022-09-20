'''
Given an input array arr containing integers, find the shortest ascending subsequence such that removing the subsequence from arr will leave arr with unique numbers only



'''


def findSubsequence(arr):
	found = set()
	sequence = []
	for i in arr:
		if i in found:
			sequence.append(i)
		else:
			found.add(i)
		  
	if len(sequence)==0:
		return [-1]
	
	sequence = sorted(sequence)
	
	i = 0
	j = 0
	
	while j < len(arr) and i < len(sequence):
		if arr[j] == sequence[i]:
			i += 1 
		j += 1
	
	if i < len(sequence):
		return [-1]
			
	return sequence

