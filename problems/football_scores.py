'''
teamA is a list of the goals of team A in each match
teamB is a list of the goals of team B in each match
2<= n, m <=10^5

For each match of team B, compute the total number of matches of team A where team A scored less than or equal to team B in that match.
'''

def count(teamA, teamB):
  dict1 = {}
  for g in teamA:
    if dict1.get(g) is None:
      dict1[g] = 1
    else:
      dict1[g] += 1

  dict2 = {}
  for g in teamB:
    count = 0
    for i in range(g, -1, -1):
      if dict2.get(i) is not None:
        count += dict2[i]
        break
      else:
        if dict1.get(i) is not None:
          count += dict1[i]
    dict2[g] = count
    
  print(dict1)
  print(dict2)
  return [dict2[g] for g in teamB]
  
if __name__=='__main__':
  teamA = [5,2,2,1,3,0]
  teamB = [0,0,0]
  print(count(teamA, teamB))