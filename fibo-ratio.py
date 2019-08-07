def fibonacci(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)


def ratio():
  ratio = []
  for i in range(1, 50, 1):
    ratio.append(fibonacci(i+1)/fibonacci(i))
  print(ratio)


ratio()
