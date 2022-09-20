'''
create dict
	key: curr char
 	val: list of following chars
recursion


if len(s) == n
	append to res list
else for char in dict[curr]
	recurse(s + char)
'''
def countVowelPermutations(n):
	follows = {
		'a': ['e'],
		'e': ['a', 'i'],
		'i': ['a', 'e', 'o', 'u'],
		'o': ['u', 'i'],
		'u': ['a'],
		'': ['a', 'e', 'o', 'u', 'i']
	}
	res = []
	def recurse(s):
		nonlocal n, res
		if len(s) == n:
			res.append(s)
		else:
			if len(s) == 0:
				key = ''
			else:
				key = s[-1]
			for char in follows[key]:
				recurse(s + char)
	
	recurse('')
	return len(res)

print(countVowelPermutations(2))