# Proof that Fibonacci Ratio is Golden Ratio.

import math

def fibonacci(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)


def ratio():
  ratio = []
  for i in range(1, 36, 1):
    ratio.append(fibonacci(i+1)/fibonacci(i))
  print(ratio)


print((1+math.sqrt(5))/2)
# ratio()
