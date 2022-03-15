#"Whats the ~th number of the Fibonacci sequence? This script will tell you"

x = int(input("Enter a number to find its Fibonacci sequence: "))
 
def fibb_seq(x):     #Method to find the number
    counter = 0      
    fib_list = []
    count_list = []

    if x <= 0:      #If spec number is 0 or negative  
        return 0

    while counter < x:
        if counter == 0:
            fib_list.insert(counter, 0)
            fib_list.insert((counter + 1), 1)
            count_list.insert(counter, 0)
            count_list.insert((counter + 1), 1)
            counter += 2
        else:
            fib_list.insert(counter, (fib_list[counter - 1] + fib_list[counter - 2]))
            count_list.insert(counter, (fib_list[counter - 1] + fib_list[counter - 2]) + count_list[counter - 1])
            counter += 1
    return count_list[x - 1]

print(fibb_seq(x))