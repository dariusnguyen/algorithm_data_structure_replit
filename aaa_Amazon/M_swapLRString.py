'''
777. Swap Adjacent in LR String
Medium

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.
 
Example 1:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

Example 2:

Input: start = "X", end = "L"
Output: false
 
Constraints:

1 <= start.length <= 104
start.length == end.length
Both start and end will only consist of characters in 'L', 'R', and 'X'.
'''

'''
if:
	the lengths of start and end are different
 	the numbers of Ls and Rs are different bw start and end
then invalid

XL can only stay the same as XL or transform to LX
RX can only stay the same as XL or transform to XR
so map the indices of L and R for each XL and RX in start
compare to the indices in end

RX XL RX RXL

RX XXX R
RR XXX X
'''

def canTransform(start, end):
	if len(start) != len(end):
		return False
		
	if start.replace('X', '') != end.replace('X', ''):
		return False

	startIndices = 
	for i in range(len(start)):
		if start[i] == 'L':
			if i-1>=0 and start[i-1]=='X':
				if not (end[i]=='L' or end[i-1]=='L'):
					return False
			else:
				if end[i]!='L':
					return False

		if start[i] == 'R':
			if i+1<len(start) and start[i+1]=='X':
				if not (end[i]=='R' or end[i+1]=='R'):
					return False
			else:
				if end[i]!='R':
					return False
	return True

s0 = "RXXLRXRXL"
e0 = "XRLXXRRLX"

s1 = "XL"
e1 = "LX"

s2 = 'RL'
e2 = 'LR'

s3 = 'XXL'
e3 = 'LXX'

s4 = 'RXL'
e4 = 'XRL'

s5 = 'RXL'
e5 = 'XLR'

s6 = 'XXXXXXL'
e6 = 'XLXXXXX'

s6 = 'XXRXXXL'
e6 = 'XXXRLXX'

s6 = 'XXLXXXL'
e6 = 'LLXXXXX'

for s, e in [(s0, e0), (s1, e1), (s2, e2), (s3, e3), (s4,e4), (s5,e5)]:
	print(canTransform(s, e))