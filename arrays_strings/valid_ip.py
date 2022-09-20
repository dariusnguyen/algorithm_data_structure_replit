'''
given an ip address string. check if it is a vadid ip address

UMPIRE
Understand
	Rules for valid Ip address:
		format x.x.x.x
		x is a number
		0<=x<=255
		between x's has to be a dot
		4 different x's
	Corner cases:
		empty string
		contains special chars other than dot
		fewer than 4 x's
	Questions:
		do spaces at the beginning or end of the string make the ip address invalid?
			if no, make sure to remove leading and trailing spaces

Match
	string processing
	conditionals
Plan
	if empty string
		return False
	splitted = split string with '.'
	for each element of list
		if not digits or not between 0, 255
			return False
	return True

Time: O(1)
Mem: O(1)

Implement
'''
def is_valid(ip: str):
	if len(ip) == 0:
		return False
	splitted = ip.strip().split('.')
	if len(splitted) !=4:
		return False
	for i in splitted:
		if i.isdigit() == False:
			return False
		num = int(i)
		if num<0 or num>255:
			return False
	return True

'''
Review
Evaluate
	Cons: many conditionals
'''