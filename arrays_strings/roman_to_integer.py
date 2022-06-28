def romanToInt(self, s: str) -> int:
  '''
  method 1:
  create a dict to map char to value
  sum = 0
  loop through string left to right
      if this is the last char:
          add char value to sum
      if char i's value is less than the next char's value:
          subtract char value from sum
      else:
          add char value to sum
  return sum
          
  Time complexity: O(n)
  Space complexity: O(1)
      
  '''
 
#         map = {'I': 1,
#               'V': 5,
#               'X': 10,
#               'L': 50,
#               'C': 100,
#               'D': 500,
#               'M': 1000}
    
#         su = 0
    
#         for i in range(len(s)):
#             val = map[s[i]]
#             if i == (len(s)-1):
#                 su += val
#             elif val < map[s[i+1]]:
#                 su -= val
#             else:
#                 su += val
    
#         return su

  '''
  method 2: just replace special cases

  time complexity: O(7n)=O(n)
  '''
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        number += translations[char]
    return number
