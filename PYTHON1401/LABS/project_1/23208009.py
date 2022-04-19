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
    return (y)

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

print(main('asymmetry_sample.csv', 'A1356', True))