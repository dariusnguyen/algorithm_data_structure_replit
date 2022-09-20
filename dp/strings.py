'''
Given a string target and an array of strings arr, write a function to return True if the string target can be constructed from some combination of strings in arr. Each string in arr can be used as many time as necessary.

Example: can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'])
Output: True, because 'abc'+'def'='abcdef'

Example: can_construct('skateboard', ['boar', 'sk', 'a', 'ate'])
Output: False

Example: can_construct('', ['ab', 's'])
Output: True
'''

'''
*U

*M
Recursion
DP

*P
Recursion:
base case: string is empty
	return True
base case: none of the strings in arr are a prefix of s
	return False
recursive case:
	check each of the strings in arr if they are a prefix
	call f() on new target after removing prefix

*I
*R
*E
'''

def can_construct_recur(target, arr):
	if target == '':
		return True

	for sub in arr:
		if sub == target[:len(sub)]:
			new_target = target[len(sub):]
			if can_construct_recur(new_target, arr):
				return True
		
	return False

def can_construct_dp(target, arr, memo={}):
	if target == '':
		return True
	if target in memo:
		return memo[target]
		
	for sub in arr:
		if sub==target[:len(sub)]:
			new_target = target[len(sub):]
			if can_construct_dp(new_target, arr, memo):
				memo[target] = True
				return True
	memo[target] = False
	return False

'''
Now create a function to count number of ways target can be constructed by strings in arr
'''

def count_construct_recur(target, arr):
	if target == '':
		return 1
	count = 0
	for sub in arr:
		if sub == target[:len(sub)]:
			new_target = target[len(sub):]
			count += count_construct_recur(new_target, arr)
	return count

def count_construct_dp(target, arr, memo={}):
	if target == '':
		return 1
	if target in memo:
		return memo[target]
		
	count = 0
	for sub in arr:
		if sub == target[:len(sub)]:
			new_target = target[len(sub):]
			count += count_construct_dp(new_target, arr, memo)
	memo[target] = count
	return count

'''
'target'
't', 'tar', 'ar', 'get', 'arg', 'et'

recursion
base case: target = ''
	return []
for sub in arr
	if sub = target[:len(sub)]
 		construct = recurse(target[len(sub):], arr)
   		construct.append(sub)
'''
def all_construct_recur(target, arr):
	if target=='':
		return [[]]
	res = []
	for sub in arr:
		if sub == target[:len(sub)]:
			construct = all_construct_recur(target[len(sub):], arr)
			if construct is not None:
				for c in construct:
					c.append(sub)
				res += construct
	return res

def all_construct_dp(target, arr, memo={}):
	'''
 	there's a bug. doesn't run correctly yet
 	'''
	if target == '':
		return [[]]
	if target in memo:
		return memo[target]
	print('target:', target)

	res = []
	for sub in arr:
		if sub == target[:len(sub)]:
			construct = all_construct_dp(target[len(sub):], arr, memo)
			print('sub', sub, 'new target:', target[len(sub):])
			print('construct', construct)
			if construct is not None:
				for c in construct:
					c.insert(0, sub)
				res += construct
				
	memo[target] = res

	# print('memo:', memo)
	return res

