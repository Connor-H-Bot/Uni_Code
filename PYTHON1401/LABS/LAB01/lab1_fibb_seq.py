x = int(input("Enter a number to find its fibonacci sequence: "))
 
def fibb_seq(x):
    iteration = x
    counter = 0
    fib_list = [x]
    for counter in x:
        if counter == 0:
            fib_list[counter] = 0
            fib_list[counter + 1] = 1
            counter += 2
        else:
            fib_list[counter] == (fib_list[counter - 1] + fib_list[counter - 2])
            counter += 1
    return fib_list[x]

print(fibb_seq(x))