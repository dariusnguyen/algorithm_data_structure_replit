'''
Given an array of numbers and a target sum, write a function to return True if the target sum can be achieved using numbers in the array. Each number can be used more than once.

Examples:
can_sum(7, [5,3,4,7])
	Output: True

can_sum(7, [2,4])
	Output: False
'''

'''
Recursive brute force method:
(refer to can_sum.draw)
'''

def can_sum_recursive(target, nums):
	if target == 0:
		return True
	if target < 0:
		return False
		
	for i in nums:
		if can_sum_recursive(target-i, nums):
			return True
	return False

'''
DP method:
memoize the result of each target value
'''

def can_sum_dp(target, nums, memo = {}):
	if memo.get(target) is not None:
		return memo[target]
	if target == 0:
		return True
	if target<0:
		return False
	
	for i in nums:
		if can_sum_dp(target-i, nums, memo):
			memo[target] = True
			return True
	memo[target] = False
	return False

def how_sum_recursive(target, nums):
	if target == 0:
		return []
	if target < 0:
		return None
	for i in nums:
		res = how_sum_recursive(target-i, nums)
		if res is not None:
			res.append(i)
			return res
	return None

def how_sum_dp(target, nums, memo={}):
	if target in memo:
		return memo[target]
	if target == 0:
		return []
	if target < 0:
		return None
	
	for i in nums:
		res = how_sum_dp(target - i, nums, memo)
		if res is not None:
			res.append(i)
			memo[target] = res
			return res
	
	memo[target] = None
	return None


def best_sum_recursive(target, nums):
	if target == 0:
		return []
	if target < 0:
		return None

	# min_length = float('inf')
	min_res = None
	
	for i in nums:
		res = best_sum_recursive(target-i, nums)
		if res is not None:
			res.append(i)
			if min_res is None or len(res) < len(min_res):
				min_res = res

	# if min_res:
	# 	return min_res

	# return None
	return min_res
	
def best_sum_dp(target, nums, memo={}):
	# print(f'target={target}')
	if target in memo:
		return memo[target]
	if target==0:
		return []
	if target<0:
		return None

	min_res = None
	# min_len = float('inf')
	
	for i in nums:
		res = best_sum_dp(target-i, nums, memo)
		if target==1:
			# print(f'target={target}')
			# print(f'memo[{target}-{i}]={memo[target-i]}')
			print()
			print(f'i={i} bestsumdp({target}-{i})={res}')
		if res is not None:
			if target==1:
				print(f'res b4 append: {res}')
			res.append(i)
			if target==1:
				print(f'res after append: {res}')
			# if target==5:
				# print('appending')
			if target==1:
				print(f'res={res} min_res={min_res}')
			if min_res is None or len(res)<len(min_res):
				min_res = res
			
			
		
	# if min_res is not None:
	# 	memo[target] = min_res
		# if target==5:
		
	if target == 1:
		print(memo)
		print(f'min_res={min_res}')
		# return min_res
	
	memo[target]=min_res
	if target == 1:
		print(memo)
	return min_res		