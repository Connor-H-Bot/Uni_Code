def trip_cost(price,distance,economy):
    economy /= 100
    total_cost = ((economy * distance) * price)
    return total_cost

def to_celsius(fahrenheit):
    """Return the given fahrenheit temperature in degrees celsius"""
    degrees_celsius = (fahrenheit - 32) * (5 / 9)
    return degrees_celsius

def days_in_years(number_of_years):
    """ Return the number of days in the given number of years, assuming
        exactly 365 days in all years.
    """
    num_days = (number_of_years * 365)
    return num_days

def calculate_cartons(eggs):
    """ Calculate the number of cartons needed to hold 
        the specified number of eggs.
    """
    cartons = (eggs // 12)
    return cartons

def dinner_calculator(meal_cost, drinks_cost):
    """ Calculate the cost of dinner during happy hour.
        Takes into consideration:
         - Pre-GST meal and drink costs
         - Happy Hour discounts
         - GST
    """
    drinks_cost *= .7
    total_cost = (meal_cost + drinks_cost) * 1.15
    return total_cost

def odd_finder(a,b,c,d,e,f,g,h,i,j):
    unfiltered_list = [a,b,c,d,e,f,g,h,i,j]
    list_index = 0
    odds_count = 0
    while list_index < len(unfiltered_list):
        if (unfiltered_list[list_index] % 2 != 0) and (unfiltered_list[list_index] >= 0):
            odds_count += 1
            list_index += 1
        else:
            list_index += 1
    return odds_count

#predict virus growth with (num = initial cases), (rate = rate of growth), (hour = hours to achive rate), (time = specify ammt of time to pass)
def virus_growth(num,rate,hour,time):
    predicted_growth = (num * pow(rate, (time / hour)))
    return predicted_growth

#A series that starts at 1^2 and finishes at n^2, adding all numbers together
def dseries(n_terms):
    dseries_count = 1
    dseries_total = 0
    if n_terms == 0:
        return 0
    while dseries_count <= n_terms:
        dseries_total += pow(dseries_count, 2)
        dseries_count += 1
    return dseries_total