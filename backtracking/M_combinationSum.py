'''
39. Combination Sum
Medium

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []


Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
'''

'''
backtracking using recursion
use a stack "currComb" to track candidates in current combinations

init result = []
recurse(target, currComb, startIndex)
base case
	if target == 0
 		append currComb to result list
   		return
	if target < 0
 		return

	loop through candidates starting from startIndex
 		add candidate to currComb
   		recurse(target - candidate, currComb, i)
	 	(after returned from recurse()) pop the candidate from currComb

'''

def combinationSum(candidates, target):
	res = []
	num_candidates = len(candidates)
	
	def recurse(target, currComb, startIndex):
		if target == 0:
			res.append(currComb.copy())
			return
		if target < 0:
			return

		for i in range(startIndex, num_candidates):
			currComb.append(candidates[i])
			recurse(target - candidates[i], currComb, i)
			currComb.pop()
			
	recurse(target, [], 0)
	return res