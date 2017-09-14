import math

# quadratic function
def quadratic(a, b, c):
    if a == 0:
        return 'INVALID: a must not be 0'

    x1 = (-b + math.sqrt(b**2 - (4*a*c))) / 2*a
    x2 = (-b - math.sqrt(b**2 - (4*a*c))) / 2*a

    if x1 == x2:
        return x1
    else:
        return x1, x2

print(quadratic(1, 0, -4))