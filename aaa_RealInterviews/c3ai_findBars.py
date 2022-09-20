# Given a number of integers in an array, each number represents a vertical bar. Write a program to
# find the two bars, which together forms a container, such that the container contains the
# most water.
#
#
# ======================
# Example 1:
# ======================
#
#
#      |
#      |
# |+---|-+-------+----+
# |    |              |
# |    |    |    |    |    |
# |    |    |    |    |    |
# +------------------------+
#
#
# ======================
# Example 2:
# ======================
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49

'''
[1,8,6,2,5,4,8,3,7]

1 8
1*1 = 1

maximize height * widtth
height = min (b0, b1)

brute force:
loop through the array(2pointers/nested loops)
calc area and save in new array
find max in area array
time complexity: O(n^2)

#
#      |
#      |
# |+---|-+-------+----+
# |    |              |
# |    |    |    |    |    |
# |    |    |    |    |    |
# +------------------------+
       |                   |


....

init 2 pointers
compare 2 pointers
move lower
calc area
save area

'''

def findBars(arr):
  l = 0
  r = len(arr)-1
  maxArea = arr[l]*arr[r]
  while l<r:
    if arr[l]<arr[r]:
      l+=1      
    else:
      r-=1
    area = arr[l]*arr[r]
    maxArea = max(maxArea, area)
  return maxArea

print(findBars(arr)
















