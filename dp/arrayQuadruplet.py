def find_array_quadruplet_recur(arr, s):
	def recurse(arr, target):
		if target == 0:
			# print('target==0')
			return []
		if target < 0:
			# print('target<0')
			return None
			
		for i in range(len(arr)):
			# print(arr, target)
			recurse_res = recurse(arr[i+1:], target - arr[i])
			# print(i, target-i, recurse_res)
			if recurse_res is not None and len(recurse_res) < 4:
				recurse_res.append(arr[i])
				return recurse_res
		return None
		
	return sorted(recurse(arr, s))

def find_array_quadruplet_dp(arr, s, memo = {}):
	def recurse(arr, target):
		if target == 0:
			# print('target==0')
			return []
		if target < 0:
			# print('target<0')
			return None
			
		for i in range(len(arr)):
			# print(arr, target)
			recurse_res = recurse(arr[i+1:], target - arr[i])
			# print(i, target-i, recurse_res)
			if recurse_res is not None and len(recurse_res) < 4:
				recurse_res.append(arr[i])
				return recurse_res
		return None
		
	return sorted(recurse(arr, s))

arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20

print(find_array_quadruplet_recur(arr, s))
# print(set(arr))