'''
You're developing a system for scheduling advising meetings with students in a Computer Science program. Each meeting should be scheduled when a student has completed 50% of their academic program.

Each course at our university has at most one prerequisite that must be taken first. No two courses share a prerequisite. There is only one path through the program.

Write a function that takes a list of (prerequisite, course) pairs, and returns the name of the course that the student will be taking when they are halfway through their program. (If a track has an even number of courses, and therefore has two "middle" courses, you should return the first one.)

Sample input 1: (arbitrarily ordered)
pairs1 = [
	["Foundations of Computer Science", "Operating Systems"],
	["Data Structures", "Algorithms"],
	["Computer Networks", "Computer Architecture"],
	["Algorithms", "Foundations of Computer Science"],
	["Computer Architecture", "Data Structures"],
	["Software Design", "Computer Networks"]
]

In this case, the order of the courses in the program is:
	0 Software Design
	1 Computer Networks
	2 Computer Architecture
	3Data Structures
	4Algorithms
	5Foundations of Computer Science
	6Operating Systems

Sample output 1:
	"Data Structures"

Sample input 2:
pairs2 = [
    ["Algorithms", "Foundations of Computer Science"],
    ["Data Structures", "Algorithms"],
    ["Foundations of Computer Science", "Logic"],
    ["Logic", "Compilers"],
    ["Compilers", "Distributed Systems"],
]

Sample output 2:
	"Foundations of Computer Science"

Sample input 3:
pairs3 = [
	["Data Structures", "Algorithms"],
]

Sample output 3:
	"Data Structures"

All Test Cases:
halfway_course(pairs1) => "Data Structures"
halfway_course(pairs2) => "Foundations of Computer Science"
halfway_course(pairs3) => "Data Structures"

Complexity analysis variables:

n: number of pairs in the input
'''
'''
Method 1: populate courselist from left to right and from right to left
	loop through the list
	build 2 dicts
	prereqsToCourse
	courseToPrereqs
	init program list starting with first pair
	populate to the left with courseToPrereqs
	populate to the right with prereqsToCourse
	return middle item
	time: O(n) where n is the length of 'pairs'
	space: O(n)
'''
# import math

def halfway_course(pairs):
	prereqToCourse = {}
	courseToPrereq = {}

	for p in pairs:
		prereqToCourse[p[0]] = p[1]
		courseToPrereq[p[1]] = p[0]

	program = [pairs[0][0], pairs[0][1]]

	next = 1
	while next:
		next = prereqToCourse.get(program[-1])
		if next:
			program.append(next)
			
	prev = 1
	while prev:
		prev = courseToPrereq.get(program[0])
		if prev:
			program.insert(0, prev)
	print(program)
	return program[int((len(program)-1)/2)]



pairs1 = [
    ["Foundations of Computer Science", "Operating Systems"],
    ["Data Structures", "Algorithms"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"],
]

pairs2 = [
    ["Algorithms", "Foundations of Computer Science"],
    ["Data Structures", "Algorithms"],
    ["Foundations of Computer Science", "Logic"],
    ["Logic", "Compilers"],
    ["Compilers", "Distributed Systems"],
 ]

pairs3 = [
    ["Data Structures", "Algorithms"],
]

print(halfway_course(pairs3))


'''
Method 2: Build a graph and use topological sorting

'''