#Input a number and this will count + add that ammount of odd numbers starting at 1

n = int(input("Enter a number: "))
 
def odd_count(n):     #Method to find the number
    counter = 1
    odds_count = 0      
    odds_total = 0

    if n <= 0:      #If spec number is 0 or negative  
        return 0
    while odds_count < n:
        odds_total += counter
        counter += 2
        odds_count += 1

    return odds_total

print(odd_count(n))