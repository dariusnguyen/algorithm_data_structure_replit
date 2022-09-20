'''
Write a program to sort a stack such that the smallest items are on top. You can use an additional temporary stack, but you may not copy elements into any other data structure (such as an array).

The stack supports the following operations : push, pop, peek, isEmpty.

Input and output are both stacks

Input : [34, 3, 31, 98, 92, 23]
Output : [3, 23, 31, 34, 92, 98]

Input : [3, 5, 1, 4, 2, 8]
Output : [1, 2, 3, 4, 5, 8]
'''

'''
		Top				Bottom
Input : [34, 3, 31, 98, 92, 23]
Output : [3, 23, 31, 34, 92, 98]

Use a temporary stack to store sorted elements
Pop from input stack while input stack is not empty
If element is smaller than element peeked in temp stack:
	push in temp stack
If element is larger                                   :
	pop elements from temp stack and push in input stack until the next peeked element in temp stack is larger

The above steps will temporary sort the input stack from largest to smallest, and the temp stack will finally be sorted from smallest to largest (top to bottom)

'''

def sort(stack):
	temp = []
	while len(stack)>0:
		curr = stack.pop()
		if len(temp) == 0 or curr < stack[-1]:
			temp.append(curr)
		else:
			while curr > stack[-1] and len(temp)>0:
				stack.append(temp.pop())
	return temp