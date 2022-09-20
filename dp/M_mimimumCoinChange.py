'''
322. Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
'''

'''
use recursion to explore all possible combinations
use dp to optimize time
'''

def minimumCoins(coins, amount):
	def recurse(nums, target, memo={}):
		if target in memo:
			return memo[target]
		if target == 0:
			return 0
		if target < 0:
			return -1 #a

		min_res = -1 #b
		#both a and b has to return -1 for c to work correctly
		for i in nums:
			res = recurse(nums, target - i, memo)
			if res != -1: #c
				res += 1
				if min_res==-1 or res < min_res:
					min_res = res
		
		memo[target] = min_res
		return min_res
	
	return recurse(coins, amount)


'''
3 - 2 = 1
1 - 2 < 0
'''