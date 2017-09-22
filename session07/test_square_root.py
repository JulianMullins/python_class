import math

def mysqrt(a):
    if a<=0:
        return 'Invalid input value'

    epsilon = 0.00000001
    x = a/2

    while True:
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            return y
        x = y

def text_square_root():
    print('a'.ljust(5) + 'mysqrt(a)'.ljust(20) + 'math.sqrt(a)'.ljust(20) + 'diff'.ljust(5))
    print(''.ljust(5, '-') + ''.ljust(20, '-') + ''.ljust(20, '-') + ''.ljust(5, '-'))
    for i in range(1, 10):
        my_root = mysqrt(i)
        calc_root = math.sqrt(i)
        diff = abs(my_root - calc_root)
        print(str(float(i)).ljust(5) + str(my_root).ljust(20) + str(calc_root).ljust(20) + str(diff).ljust(5))

text_square_root()