# return absolute value of integer or float
def my_abs(x):
    if isinstance(x, (int, float)):
        return(abs(x))

print(my_abs('blah'))