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
    if type == 'stats' and isinstance(adults, str): #Check if input is stats and user input a string
        file_output = get_adult(csvfile, adults)
        output_converted = make_2d(file_output)
        asym3d1 = asymmetry_analysis(output_converted)
        mn1 = get_min_asymmetry(asym3d1)
        mx1 = get_max_asymmetry(asym3d1)
        avg1 = get_avg_asymmetry(asym3d1)
        std1 = False 
        return list_rounder(asym3d1), mn1, mx1, avg1, std1
    elif type == 'corr' and isinstance(adults, list): #Check if type is corr and user input a list
        return False
    else: 
        return False 
    

#Retrieves selected adult from the csvfile. 
#Reads line by line, so it works if theres gaps between required rows
def get_adult(filename, substring):
    file_read = open(filename, 'r')
    getline = file_read.readline()
    adult = []
    while getline:
        if substring in getline and len(adult) <= 10: #stop after 10 entries
            adult.append(getline)
            getline = file_read.readline()
        elif len(adult) <= 10:
            getline = file_read.readline()
    file_read.close()
    return adult

#convert selected adult data into a 2D list
def make_2d(list):
    list_in_2d = [[0] * 3 for i in range(10)] #initialise 2d list (3x, 10y)
    input_list_index = 0                      #index counter for input array
    while input_list_index < len(list): 
        new_2D_index, facial_point_index = 0, 2
        facial_point_iteration = list[input_list_index]            #create instance variable to a single facial points x,y,z values
        facial_point_iteration = facial_point_iteration.replace('\n', '')
        facial_point_iteration = facial_point_iteration.split(',') #remove carriage return and split using commas
        while new_2D_index < 3:
            list_in_2d[input_list_index][new_2D_index] = facial_point_iteration[facial_point_index]
            new_2D_index += 1
            facial_point_index += 1  
        input_list_index += 1
    return list_in_2d  

# Calibrate data and perform asymmetry analysis
def asymmetry_analysis(list_in_2d):
    float_list = [[float(element) for element in list_inner] for list_inner in list_in_2d] #convert all numbers to floats
    asymmetry_analysis_list = [] #list to store values for each facial points analysis
    is_nosevalue_nonzero = [float_list[9][0] or float_list[9][1] or float_list[9][2] != 0] #returns true if nose offset is needed
    if  all(is_nosevalue_nonzero): #When nose offset needed
        x_offset, y_offset, z_offset = float_list[9][0], float_list[9][1], float_list[9][2]
        del float_list[9]
        for index in range(len(float_list)):
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
    return asymmetry_analysis_list

# Return a list with the lowest asymmetry values for upper and lower face
def get_min_asymmetry(asymmetry_analysis_list):
    min_asymmetry = [asymmetry_analysis_list[0], asymmetry_analysis_list[5]]  
    for index in range(len(asymmetry_analysis_list)):
        current_number = asymmetry_analysis_list[index]
        # Rules lists that == True when conditions are met. "first_half.." is for upper face values, "second_half.." for lower. 
        first_half_rules = [(index < 4) and (asymmetry_analysis_list[index + 1] > current_number < min_asymmetry[0])]
        second_half_rules = [4 < index < 8 and min_asymmetry[1] > current_number < asymmetry_analysis_list[index + 1]]
        if all(first_half_rules):
            min_asymmetry[0] = current_number
        if (index == 4) and (current_number < min_asymmetry[0]):
            min_asymmetry[0] = current_number
        if all(second_half_rules):
            min_asymmetry[1] = current_number
        if (index == 8) and (current_number < min_asymmetry[1]):
            min_asymmetry[1] = current_number
    return list_rounder(min_asymmetry)

# Return a list with the highest asymmetry values for upper and lower face
def get_max_asymmetry(asymmetry_analysis_list):
    max_asymmetry = [0.0, 0.0]  
    for index in range(len(asymmetry_analysis_list)):
        current_number = asymmetry_analysis_list[index]
        first_half_rules = [(index < 4) and (asymmetry_analysis_list[index + 1] < current_number > max_asymmetry[0])]
        second_half_rules = [4 < index < 8 and max_asymmetry[1] < current_number > asymmetry_analysis_list[index + 1]]
        if all(first_half_rules):
            max_asymmetry[0] = current_number
        if (index == 4) and (current_number > max_asymmetry[0]):
            max_asymmetry[0] = current_number
        if all(second_half_rules):
            max_asymmetry[1] = current_number
        if (index == 8) and (current_number > max_asymmetry[1]):
            max_asymmetry[1] = current_number
    return list_rounder(max_asymmetry)

# Return a list with the average asymmetry values for upper and lower face
def get_avg_asymmetry(asymmetry_analysis_list):
    avg_asymmetry = [0.0, 0.0] #Declare the output list with values
    for index in range(len(asymmetry_analysis_list)): 
        if index < 5:
            avg_asymmetry[0] += asymmetry_analysis_list[index]
            if index == 4:
                avg_asymmetry[0] /= 5 
        if 4 < index < len(asymmetry_analysis_list):
            avg_asymmetry[1] += asymmetry_analysis_list[index]
            if index == 8:
                avg_asymmetry[1] /= 4
                rounded_avg_asymmetry = []
                rounded_avg_asymmetry.append(round(avg_asymmetry[0], 4))
                rounded_avg_asymmetry.append(round(avg_asymmetry[1], 4))
    return list_rounder(avg_asymmetry)

# Function to round all numbers in a 1d list
def list_rounder(list_to_round):
    list_rounded = []
    for index in range(len(list_to_round)): #iterate through every index
        list_rounded.append(round(list_to_round[index], 4))
        index += 1
    return list_rounded

print(main('asymmetry_sample.csv', 'C4996', 'stats'))
