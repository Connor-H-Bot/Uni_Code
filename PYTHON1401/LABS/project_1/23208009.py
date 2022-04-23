# Author: Connor Harris
#
# Project 1 for CITS1401. 
# This script is used to perform a statistical analysis or correlation analysis on facial symmetry using an XYZ axis. 
#
# Takes the following input:
#   -csvfile - The initial file to run this script on.
#   -adults - The specified adult using their ID, or a list of two adults.
#   -*Type* - "stats" or "corr" arguments:
#       -stats - Perform statistical analysis on a single adult.
#       -corr - Perform correlation analysis of the two specified adults with a list.

def main(csvfile, adults, type):
    stats_rules = [type == 'stats' and isinstance(adults, str)] # == True if conditions for stats input are satisfied
    corr_rules = [type == 'corr' and isinstance(adults, list) and len(adults) == 2] # == True if conditios for correlation input satisfied
    if all(stats_rules): #Check if input is stats and user input a string
        file_output = get_adult(csvfile, adults)
        output_converted = make_2d(file_output)
        asym3d1 = asymmetry_analysis(output_converted)
        mn1 = get_min_asymmetry(asym3d1)
        mx1 = get_max_asymmetry(asym3d1)
        avg1 = get_avg_asymmetry(asym3d1)
        std1 = get_stddev(avg1, asym3d1)
        all_zero_values = [index == 0 for index in asym3d1] #Test case for all zeros in asym3d list
        if all(all_zero_values):
            print("Error: Please check the input arguments")
            return [], [], [], [], [] #Return empty lists
        return list_rounder(asym3d1), mn1, mx1, list_rounder(avg1), std1
    elif all(corr_rules): #Check if type is corr and user input a list
        a1_output, a2_output = get_adult(csvfile, adults[0]), get_adult(csvfile, adults[1])
        a1_converted, a2_converted = make_2d(a1_output), make_2d(a2_output)
        a1_analysis, a2_analysis = asymmetry_analysis(a1_converted), asymmetry_analysis(a2_converted)
        adults_corr = get_correlation(a1_analysis, a2_analysis)
        return adults_corr
    else: #Else case to return 5x empty lists
        print("Error: Please check the input arguments")
        return [], [], [], [], []
    
# Create profile

#Retrieves selected adult from the csvfile. 
#Reads line by line, so it works if theres gaps between required rows
def get_adult(filename, substring):
    file_read = open(filename, 'r')
    getline = file_read.readline()
    adult = []
    while getline: #Iterates through entire document until 
        if substring in getline and len(adult) <= 10: #stop after 10 entries
            adult.append(getline)
            getline = file_read.readline()
        elif len(adult) <= 10:
            getline = file_read.readline()
    file_read.close()
    return adult #returns list with each index containing a row

#convert selected adult data into a 2D list and removes name column
def make_2d(list):
    list_in_2d = [[0] * 4 for i in range(10)] #initialise 2d list (3x, 10y)
    input_list_index = 0                      #index counter for input array
    while input_list_index < len(list): 
        new_2D_index, facial_point_index = 0, 1 #facial point starts at [1] so that it doesnt take the first column [0] that only contains adultID
        facial_point_iteration = list[input_list_index]            #create instance variable to a single facial points x,y,z values
        facial_point_iteration = facial_point_iteration.replace('\n', '')
        facial_point_iteration = facial_point_iteration.split(',') #remove carriage return and split using commas
        while new_2D_index < 4: #Iterate through by adding each rows point number & XYZ values first
            list_in_2d[input_list_index][new_2D_index] = facial_point_iteration[facial_point_index]
            new_2D_index += 1
            facial_point_index += 1  
        input_list_index += 1
    return list_in_2d #Returns 2D list, with sub indexes referring to each facial point and their XYZ values

# Calibrate data and perform asymmetry analysis
def asymmetry_analysis(list_in_2d):
    float_list = [[float(element) for element in list_inner] for list_inner in list_in_2d] #convert all numbers to floats
    float_list.sort(key=lambda float_list: (float_list[0])) #Sort list by face value points
    for index in range(len(float_list)): #Remove face value points
        del float_list[index][0]
    asymmetry_analysis_list = [] #list to store values for each facial points analysis
    is_nosevalue_nonzero = [float_list[9][0] or float_list[9][1] or float_list[9][2] != 0] #returns true if nose offset is needed
    if  all(is_nosevalue_nonzero): #When nose offset needed
        x_offset, y_offset, z_offset = float_list[9][0], float_list[9][1], float_list[9][2]
        del float_list[9]
        for index in range(len(float_list)): #Minus the offset everytime (works for both negative and positive values)
            float_list[index][0] -= x_offset 
            float_list[index][1] -= y_offset
            float_list[index][2] -= z_offset
    else: #No nose offset neeeded. Remove values
        del float_list[9]
    analysis_index = 0 
    while analysis_index < len(float_list): #Iterate through entire list and use asymmetry formula for each xyz point
        x_value, y_value, z_value = float_list[analysis_index][0], float_list[analysis_index][1], float_list[analysis_index][2]
        asymmetry_analysis_list.append((x_value**2 + y_value**2 + z_value**2) ** 0.5) #sqrt(x^2 + y^2 + z^2)
        analysis_index += 1
    return asymmetry_analysis_list #Returns 1D list with non rounded asymmetry values as these will be needed for further calculations

# Return a list with 2x values, upper and then lower face asymmetry. 
def get_min_asymmetry(asymmetry_analysis_list):
    min_asymmetry = [asymmetry_analysis_list[0], asymmetry_analysis_list[5]]  #Start off at the first point value of upper/lower face
    for index in range(len(asymmetry_analysis_list)):
        current_number = asymmetry_analysis_list[index]
        # Rules lists that return True when conditions are met. "first_half.." is for upper face values, "second_half.." for lower. 
        first_half_rules = [(index < 4) and (asymmetry_analysis_list[index + 1] > current_number < min_asymmetry[0])]
        second_half_rules = [4 < index < 8 and min_asymmetry[1] > current_number < asymmetry_analysis_list[index + 1]]
        if all(first_half_rules): 
            min_asymmetry[0] = current_number
        if (index == 4) and (current_number < min_asymmetry[0]): #Exception for boundary that falls outside rules list
            min_asymmetry[0] = current_number
        if all(second_half_rules):
            min_asymmetry[1] = current_number
        if (index == 8) and (current_number < min_asymmetry[1]): #Exception for boundary that falls outside rules list
            min_asymmetry[1] = current_number
    return list_rounder(min_asymmetry) #Round list values as they are not used for further calculations

# Return a list with 2x values, which are the most asymmetric points on the upper and lower face respectively
def get_max_asymmetry(asymmetry_analysis_list):
    max_asymmetry = [0.0, 0.0]  #Starts the list with 0 as a neutral value
    for index in range(len(asymmetry_analysis_list)):
        current_number = asymmetry_analysis_list[index] 
        # Rules for the upper and lower face that returns True if "current_number" is larger than all before it and the number after it
        first_half_rules = [(index < 4) and (asymmetry_analysis_list[index + 1] < current_number > max_asymmetry[0])]
        second_half_rules = [4 < index < 8 and max_asymmetry[1] < current_number > asymmetry_analysis_list[index + 1]]
        if all(first_half_rules):
            max_asymmetry[0] = current_number
        if (index == 4) and (current_number > max_asymmetry[0]): #Exception for boundary that falls outside rules list
            max_asymmetry[0] = current_number
        if all(second_half_rules):
            max_asymmetry[1] = current_number
        if (index == 8) and (current_number > max_asymmetry[1]): #Exception for boundary that falls outside rules list
            max_asymmetry[1] = current_number
    return list_rounder(max_asymmetry) #Round list values as they are not used for further calculations

# Return a list with the average asymmetry values for upper and lower face
def get_avg_asymmetry(asymmetry_analysis_list):
    avg_asymmetry = [0.0, 0.0] #Declare the output list with 0 values
    for index in range(len(asymmetry_analysis_list)): #Iterate while index is less than the length of the list
        if index < 5: #While index is looking at upper face values ([0-4])
            avg_asymmetry[0] += asymmetry_analysis_list[index] #Add each value 
            if index == 4: #When the final index point is reached for upper face divide by total ammount
                avg_asymmetry[0] /= 5 
        if 4 < index < len(asymmetry_analysis_list): #While index is looking at lower face values (except for final one)
            avg_asymmetry[1] += asymmetry_analysis_list[index] #Add each value
            if index == 8: #When the final index point is reached for lower face divide by total ammount
                avg_asymmetry[1] /= 4
    return avg_asymmetry #List is not rounded as it will be used for standard deviation calculation 

# Return a list with 2x values; standard deviation for upper and lower face
def get_stddev(avg_asymmetry, asymmetry_3d): #requires average asymmetry for the calculation
    standard_deviations = []
    upper_mean, lower_mean = avg_asymmetry[0], avg_asymmetry[1] #Stores averages as two floats instead of accessing the list each time
    upper_face_values, lower_face_values = asymmetry_3d[0:5], asymmetry_3d[5:9] #Breaks asymmetry list into two smaller lists, upper & lower face
    upper_devs, lower_devs = 0, 0
    for index in range(len(upper_face_values)):
        if index < 5:
            upper_devs += (upper_face_values[index] - upper_mean)**2
        if index < 4:
            lower_devs += (lower_face_values[index] - lower_mean)**2
    standard_deviations.append((upper_devs / len(upper_face_values))**0.5)
    standard_deviations.append((lower_devs / len(lower_face_values))**0.5)
    return list_rounder(standard_deviations) #Round list values as they are not used for further calculations

# Function to round all numbers in a 1d list
def list_rounder(list_to_round):
    list_rounded = []
    for index in range(len(list_to_round)): #iterate through every index
        list_rounded.append(round(list_to_round[index], 4))
        index += 1
    return list_rounded

# Function to calculate correlation using r = ... formula. 
def get_correlation(adult_1_asymmetry, adult_2_asymmetry):
    adult_1_avg, adult_2_avg, eq_numerator, x_denominator, y_denominator = 0, 0, 0, 0, 0 #X and Y denoms represent denoms in correlation formula
    for index in range(len(adult_1_asymmetry)):
        adult_1_avg += adult_1_asymmetry[index] 
        adult_2_avg += adult_2_asymmetry[index]
    adult_1_avg /= len(adult_1_asymmetry)   #Find the average of the value set
    adult_2_avg /= len(adult_2_asymmetry)
    for index in range(len(adult_1_asymmetry)): 
        eq_numerator += (adult_1_asymmetry[index] - adult_1_avg) * (adult_2_asymmetry[index] - adult_2_avg) #Sum of all numerator values
        x_denominator += (adult_1_asymmetry[index] - adult_1_avg) ** 2 #Sum denom X values
        y_denominator += (adult_2_asymmetry[index] - adult_2_avg) ** 2 #Sum denom Y values
    correlation = eq_numerator / (x_denominator * y_denominator) ** 0.5 #numerator / sqrt(x_summ^2 * y_summ^2)
    return round(correlation, 4) #returns rounded value
