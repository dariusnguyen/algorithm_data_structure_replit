'''
68. Text Justification
Hard

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:

1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
'''

'''
loop through array of words until reaching the end
keep track of total length
for first word, add num chars in word
for subsquent words, add 1 + num chars in word
until total length > max width
num spaces = max width - sum of word chars
avg space = floor (num spaces / num slots (=num words - 1))
add words to temp array
add avg spaces to temp array
while there are spaces remaining in num space, add 1 to each slot

last line happens when reach the end of words array
for the last line,
add words to temp array
add 1 space between words
fill spaces until reach max width

time: depends on num words total num char, max width O(num words + total num chars/max widths)
space: O(max width + total numchars + num spaces)

Edge case: one or more words does not fit on a line
'''

'''
My naive implementation
'''
def fullJustify(words, maxWidth):
	#define left justify function for the last line and lines with only 1 word
	def leftJustify(lineWords, maxWidth):
		newLine = ''
		for w in lineWords:
			newLine += w + ' '
		newLine += ' ' * (maxWidth - len(newLine)) #fill spaces until reach maxWidth
		if len(newLine)>maxWidth: #in case the last word is exactly equal to maxWidth, need to remove the extra space added
			newLine = newLine.strip()
		return newLine
		
	numWords = len(words)
	i = 0
	l = 0
	lineWords = []
	output = []
	
	while i < numWords:
		currWord = words[i]

		if l == 0: #if this is the first word on the line, add it
			lineWords.append(currWord)
			l += len(currWord)
			i+=1
		elif ( l + 1 + len(currWord) ) <= maxWidth: #if this is not the first word on the line, and adding it and a space will not exceed maxWidth, add it and account for the space
			lineWords.append(currWord)
			l += len(currWord) + 1
			i+=1
			# if len(lineWords) != 0:
			# 	l+=1
		else: #adding the word and 1+ space will exceed maxWidth, so the line is full
			numWordsInLine = len(lineWords)
			if numWordsInLine==1:
				output.append(leftJustify(lineWords, maxWidth))
			else:
				numSpaceSlots = numWordsInLine - 1
				numSpaces = maxWidth - sum([len(w) for w in lineWords])
				spaceSlots = ['' for _ in range(numSpaceSlots)]
				
				j = 0
				#add spaces in round-robin
				while numSpaces > 0:
					spaceSlots[j % numSpaceSlots] += ' '
					numSpaces -= 1
					j += 1
					
				newLine = ''
				for k in range(numWordsInLine):
					newLine += lineWords[k]
					if k!=numWordsInLine-1: #if this is not the last word on the line, add the spaces
						newLine += spaceSlots[k]
						
				output.append(newLine)

			#reset l and lineWords for the next iteration
			l = 0
			lineWords = []
		
	# if there are words yet added to output, then process last line
	if l>0:
		output.append(leftJustify(lineWords, maxWidth))
	
	return output


'''
Improved implementation, but the idea is the same
'''

def fullJustify2(words, maxWidth):
	output, lineWords, lineChars = [], [], 0
	for word in words:
		'''
		if total num chars of words already in lineWords (lineChars)
		+  num chars of this word (len(word))
		+  num spaces needed (which is len(lineWords) because this word has not been added)
		exceeds maxWidth, then the line is full and needs to be processed first
		before adding this word
		'''
		if lineChars + len(word) + len(lineWords) > maxWidth:
			numSpaces = maxWidth - lineChars
			numSpaceSlots = max(len(lineWords) - 1, 1) #numSpaceSlots = len(lineWords)-1. When there is only 1 word, max(, 1) returns 1 to prevent modulo by 0
			for i in range(numSpaces):
				j = i % numSpaceSlots
				lineWords[j] += ' '
				
			output.append(''.join(lineWords))
			
			lineWords, lineChars = [], 0

		lineWords.append(word)
		lineChars += len(word)
	
	if lineChars > 0:
		lastLine = ' '.join(lineWords)
		lastLine += ' ' * (maxWidth - len(lastLine))
		output.append(lastLine)
	
	return output
		
