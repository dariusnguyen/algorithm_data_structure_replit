def printS(s):
	for i in range(len(s)):
		print(i, end='')
	print()
	print(s)

	mismatch = []
	l = 0
	r = len(s)-1
	while l < r:
		if s[l] != s[r]:
			mismatch.append([l,r])
		l += 1
		r -= 1
		
	mismatch_flat = sum(mismatch,[])
	for i in range(len(s)):
		if i in mismatch_flat:
			print('n', end='')
		else:
			print('y', end='')
	print('\nmismatch:', mismatch)

def minSwaps(s):
	s = list(s)
	# mismatch = []
	count = 0
	l = 0
	r = len(s)-1
	while l < r:
		if s[l] != s[r]:
			count += 1
			# mismatch.append([l,r])
		l += 1
		r -= 1
		
	if count % 2 == 1:
		if len(s) % 2 == 0:
			return -1
		else:
			return count // 2 + 1
	
	return count / 2

s = '01010111101'
printS(s)
print(minSwaps(s))