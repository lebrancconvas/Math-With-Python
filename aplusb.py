import math

def square(a,b):
    return math.sqrt(a**2 + b**2 + 2*a*b)

def cube(a,b):
    return (a**3 + b**3 + 3*(a**2)*b + 3*a*(b**2)) ** (1/3)

print(square(1.5,2.8))

print(cube(1.4,2.2))

