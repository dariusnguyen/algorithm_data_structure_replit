def getBox(r, c):
	return r//3*3 + c//3

for r in range(9):
	for c in range(9):
		print(f'{(r,c)} --> {getBox(r,c)}')