def drawLine(x0, y0, x1, y1):
	print(f'Line {(x0, y0)} --> {(x1, y1)}')

def drawHTree(x, y, length, depth):
	if depth <= 0:
		return 
	
	drawLine(x - length/2, y, x + length/2, y)
	drawLine(x - length/2, y + length/2, x - length/2, y - length/2)
	drawLine(x + length/2, y + length/2, x + length/2, y - length/2)
	
	drawHTree(x - length/2, y + length/2, length/(2**(1/2)), depth - 1)
	drawHTree(x - length/2, y - length/2, length/(2**(1/2)), depth - 1)
	drawHTree(x + length/2, y + length/2, length/(2**(1/2)), depth - 1)
	drawHTree(x + length/2, y - length/2, length/(2**(1/2)), depth - 1)

drawHTree(0, 0, 2, 1)
		