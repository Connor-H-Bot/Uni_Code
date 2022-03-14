x = int(input("Enter a number to find its factorial: "))

def x_factorise(x):
    if x == 0:
        return 1
    else:
        i = x 
    x_factorised = x
    while i > 1:
        x_factorised = (x_factorised * (i-1))
        i -= 1
    else:
        return x_factorised

print(x_factorise(x))