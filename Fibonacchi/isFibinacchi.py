#  Have the function FibonacciChecker(num) return the string yes if the number given is part of the Fibonacci sequence. This sequence is defined by: Fn = Fn-1 + Fn-2, which means to find Fn you add the previous two numbers up. The first two numbers are 0 and 1, then comes 1, 2, 3, 5 etc. If num is not in the Fibonacci sequence, return the string no. 

import math
def MathChallenge(n):

  # code goes here
  first=5*pow(n,2)+4
  second=5*pow(n,2)-4
  out=False
  for i in [first,second]:
    sroot=int(math.sqrt(i))
    if sroot*sroot==i:
      out=True

  return 'yes' if out else 'no'

# keep this function call here 
print MathChallenge(raw_input())