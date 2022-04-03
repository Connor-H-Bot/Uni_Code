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

#4: input cost and savings. If the cost is < 5% of savings return true, else return false
def buy_goods(cost, savings):
    if (cost or savings) <= 0: #get rid of any 0 or negative inputs
        return False
    elif (savings * 0.05) > cost:
        return True
    else:
        return False

#5: Return "found him" if inputs match predetermined AGL (Age, Gender, Location) 
def record_check(age, gender, location):
    if ((age > 18) and gender == "M" and (location == ("Perth") or location == ("Sydney"))):
        print("Found him!")
    else: 
         print("Did not find him.")

#6: Return list if length is even, or repeats the final element and returns
def balance_list(items):
    list_length = len(items)
    if (list_length % 2) == 0:
        return items
    else:
        items.append(items[list_length - 1])
        return items

#7: Repeat an entire list if length is even, or repeat final element if length is odd
def double_list(items):
    list_length = len(items)
    if (list_length % 2) == 0:
        items.extend(items)
        return items
    else:
        items.append(items[list_length - 1])
        return items

#8: Return true if two input words are anagrams, otherwise false
def are_anagrams(word1, word2):
    if word1 == word2:
        return False
    word1_list = list(word1)
    word1_list.sort()
    word2_list = list(word2)
    word2_list.sort()
    if word1_list == word2_list:
        return True
    else:
        return False

#9: Return index if age and name have a match. No error handling needed 
def locate_person(age_list, name_list, age, name):
    index = 0
    while index < len(age_list):
        if (age_list[index] == age) and (name_list[index] == name):
            return index
        else:
            index += 1

#10: Returns ammount of animals hunted based on weather, num of bullets used and animal type
def hunting_animals(weather, animal, n):
    if weather == "sunny" and animal == "rabbit":
        return n
    elif (weather == "rainy" and animal == "rabbit") or (weather == "sunny" and animal == "deer"):
        return int(n/2)
    elif weather == "rainy" and animal == "deer":
        return int(n/3)

#11: converts temp from cel to fahr and checks if its more or less than the limit
def check_temperature(temperature, limit):
    fahrenheit = temperature * 9 / 5 + 32
    if fahrenheit < limit:
        return True
    else:
        return False
