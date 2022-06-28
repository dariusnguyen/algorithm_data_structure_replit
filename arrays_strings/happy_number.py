'''
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Enample 1:

Input: n = 19
Output: true
Enplanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Enample 2:

Input: n = 2
Output: false
'''

'''
loop through sequence:
while (true):
  create set of digits
  sum squares of digits
  if sum==1:
    return true
  else if set of digits have been encountered b4:
    return false
  add set of digits to list
  update number
'''

def happy_number(n):
  # method 1: loop
  # list_digits = []
  # while True:
  #   # print(list_digits)
  #   digits = sorted([int(i) for i in str(n)])
  #   # print(digits)
  #   if digits in list_digits:
  #     return False      
  #   list_digits.append(digits)
  #   s = sum([i**2 for i in digits])
  #   if s == 1:
  #     return True
  #   n = s

  # method 2: recursion
  list_digits = []
  def happy_number(n, list_digits):
    digits = sorted([int(i) for i in str(n)])
    if digits in list_digits:
      return False
    s = sum([i**2 for i in digits])
    if s == 1:
      return True
    list_digits.append(digits)
    return happy_number(s, list_digits)

  return happy_number(n, list_digits)