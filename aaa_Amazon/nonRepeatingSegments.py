'''
aabcdea
a|abcde|a


abacaea
a bac ae a

loop through string
	if char in set
 		append curr segment to res
   		reset segment and set
	 
	(always) add char i to set
 	(always) add char to segment
 
'''

def nonRepeatingSegments(s):
	found = set()
	segment = ''
	res = []
	for i in s:
		if i in found:
			res.append(segment)
			segment = ''
			found = set()
		found.add(i)
		segment += i
		
	if segment != '':
		res.append(segment)
	return res

s0 = 'aabcdea'
s1 = 'abacaea'
s2 = 'a'
s3 = ''
s4 = 'aaaa'

for i in [s0, s1, s2, s3, s4]:
	print(nonRepeatingSegments(i))
	