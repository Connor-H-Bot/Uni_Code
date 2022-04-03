#1: Take user input and tell them if the number is positive, negative, or 0
userInput = input()

def my_abs(userInput):
    int(userInput)
    if userInput > 0:
        return "positive"
    elif userInput == 0:
        return "zero"
    elif userInput < 0:
        return "negative"

#2: Take user input and tell if its an odd or even number
number = input()

def is_odd(number):
    int(number)
    if number % 2 == 0:
        return False
    elif ((number % 2) > 0) or ((number % 2) < 0): #works on pos or neg 
        return True

#3: Takes input from bmi and age and tells you if your risk is low, med, or high
bmi, age = input().split()

def bmi_risk(bmi, age):  
    float(bmi, age)

    if (bmi < 22 and age < 45):
        return "Low"
    elif (bmi >= 22 and age < 45) or (bmi < 22 and age >= 45):
        return "Medium"
    else:
        return "High"
