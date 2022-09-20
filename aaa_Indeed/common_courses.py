
def find_pairs(e):
    courseToIds = {}
    ids = set()
    for i in e:
        # print(i[0], i[1])
        id = i[0]
        course = i[1]
        
        if course in courseToIds:
            courseToIds[course].append(id)
        else:
            courseToIds[course] = [id]
        ids.add(id)
        
    ids = list(ids)
    # print(ids)
    res = {}
    for i in range(len(ids)):
        # ids2 = ids.remove(i1)
        for j in range(i+1, len(ids)):
            # print(i, j)
            i1 = ids[i]
            i2 = ids[j]
            for k, v in courseToIds.items():
                if i1 in v and i2 in v:
                    if (i1,i2) in res:
                        res[i1,i2].append(k)
                    else:
                        res[i1,i2] = [k]
    for i in range(len(ids)):
        for j in range(i+1, len(ids)):
            i1 = ids[i]
            i2 = ids[j]
            if (i1, i2) not in res:
                res[(i1,i2)] = []
    return res

    
    
enrollments1 = [
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
  ["58", "Software Design"],
]

enrollments2 = [
  ["0", "Advanced Mechanics"],
  ["0", "Art History"],
  ["1", "Course 1"],
  ["1", "Course 2"],
  ["2", "Computer Architecture"],
  ["3", "Course 1"],
  ["3", "Course 2"],
  ["4", "Algorithms"],
]

enrollments3 = [
  ["23", "Software Design"], 
  ["3", "Advanced Mechanics"], 
  ["2", "Art History"], 
  ["33", "Another"],
]

print(find_pairs(enrollments1))
print(find_pairs(enrollments2))
print(find_pairs(enrollments3))



'''
Given a list of students' enrollments in courses offered by a university, return the courses taken by 
enrollments1 = [
  ["58", "Linear Algebra"],
  ["94", "Art History"],
  ["94", "Operating Systems"],
  ["17", "Software Design"],
  ["58", "Mechanics"],
  ["58", "Economics"],
  ["17", "Linear Algebra"],
  ["17", "Political Science"],
  ["94", "Economics"],
  ["25", "Economics"],
  ["58", "Software Design"],
]

enrollments2 = [
  ["0", "Advanced Mechanics"],
  ["0", "Art History"],
  ["1", "Course 1"],
  ["1", "Course 2"],
  ["2", "Computer Architecture"],
  ["3", "Course 1"],
  ["3", "Course 2"],
  ["4", "Algorithms"],
]

enrollments3 = [
  ["23", "Software Design"], 
  ["3", "Advanced Mechanics"], 
  ["2", "Art History"], 
  ["33", "Another"],
]


'''