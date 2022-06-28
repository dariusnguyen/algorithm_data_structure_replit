'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

'''
3 5 6 9 10 12 15 18 20

3 6 9 12 15 
 5 10 15 20 25
1+2+3+...+n = n(n+1)/2
3(1+2+3+...+333)
5(1+2+3+...+199)
-3*5*(1+2+3+...+66)

sumof3mul = 3*(333*334)/2
sumof5mul = 5*(199*200)/2
sumof35mul = 3*5*(66*67)/2
return sumof3mul + sumof5mul - sumof35mul
'''
def sumof35multiples(below = 1000):
  n1 = below // 3 if below % 3 !=0 else below / 3 - 1
  n2 = below // 5 if below % 5 !=0 else below / 5 - 1
  n3 = below // 15 if below % 15 !=0 else below / 15 - 1
  sumof3mul = 3 * n1 * (n1 + 1) / 2
  sumof5mul = 5 * n2 * (n2 + 1) / 2
  sumof35mul = 3 * 5 *  n3 * (n3 + 1) / 2
  return sumof3mul + sumof5mul - sumof35mul

if __name__=='__main__':
  below = 1000
  print(sumof35multiples(below))