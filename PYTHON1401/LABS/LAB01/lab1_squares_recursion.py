x = int(input("Enter a number to find its factorial: "))
 
def square_sum(x):
    totalSum = 0

    if x == 0:
        return 0

    while x != 0:
        totalSum += (x * x)
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1  
    
    return totalSum

print(square_sum(x))