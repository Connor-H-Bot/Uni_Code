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
    x = get_adult(csvfile, adults)
    y = make_2d(x)
    z = asymmetry_analysis(y)
    return z

#Retrieves selected adult from the csvfile
def get_adult(filename, substring):
    file_read = open(filename, 'r')
    getline = file_read.readline()
    adult = []
    while getline:
        if substring in getline and len(adult) <= 10: #stop at 10 entries
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
    if (float_list[9][0] or float_list[9][1] or float_list[9][2]) != 0: #Check if nose has any values != 0
        x_offset, y_offset, z_offset = float_list[9][0], float_list[9][1], float_list[9][2]
        del float_list[9]
        for index in range(len(float_list)):
            float_list[index][0] -= x_offset
            float_list[index][1] -= y_offset
            float_list[index][2] -= z_offset
    else: #remove nose elements from list
        del float_list[9]
    analysis_index = 0
    while analysis_index < len(float_list): #Iterate through entire list and use asymmetry formula for each point
        x_value, y_value, z_value = float_list[analysis_index][0], float_list[analysis_index][1], float_list[analysis_index][2]
        asymmetry_analysis_list.append((x_value**2 + y_value**2 + z_value**2) ** 0.5) #sqrt(x^2 + y^2 + z^2)
        analysis_index += 1
    return asymmetry_analysis_list

print(main('asymmetry_sample.csv', 'C4996', 'stats'))
