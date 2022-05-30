# Author: Connor Harris
#
#       Project 2 for CITS1401. 
#       This script takes in a CSV file, and a list of two adult ID's from the file and returns the following data:
#           -op1: The euclidian distances of 10x predetermined facial points (using a mix of the 15 facial points provided), for both adults
#           -op2: The cosine similarity between adult 1 and adult 2. 
#           -op3: 5 faces with the closest cosine value to adult 1, and then adult 2 respectively
#           -op4: Create a dictionary containing the averages of all 10 euclidian measurements for the 5 most similar faces (returned from op3)
#                 and do this for both adults. 

#main function to trigger the chain reaction of functions
def main(csv, adults_array): 

    if (len(adults_array) != 2) or (isinstance(adults_array, list) == False): #When the input array doesn't contain two indexes, or isnt an array
        print("Error: Second argument requires a list containing two adults from the file")
        return None, None, None, None, None #Return empty lists
    elif (adults_array[0] == adults_array[1]): #When the user input the same adult twice
        print("Error: Cannot perform comparison on two instances of the same adult. ")
        return None, None, None, None, None #Return empty lists
    elif isinstance(csv, str) == False: #when the input csv file is not a string, turn it into one
        str(csv)

    while True:
        try:
            adult_1 = make_2d(get_adult(csv, adults_array[0])) #initialises the first and second adults
            adult_2 = make_2d(get_adult(csv, adults_array[1])) 
            adult_1_euc = euc_analysis(adult_1) #does a euc analysis on the two adults, holds values for later analysis
            adult_2_euc = euc_analysis(adult_2)
            op1 = (dict_rounder(adult_1_euc), dict_rounder(adult_2_euc)) #Returns a rounded output for the euclidian distance measurements on adult 1 and 2
            op2 = round(cos_similarity(adult_1_euc, adult_2_euc), 4)    #Returns the cosine similarity of the two adults
            op3 = get_all_adults(csv, adult_1, adult_2)                #Gets all adults from the file and returns the 5 closest to each input arg adult using cosine similarity
            op4 = avg_facial_distances(op3, csv)                      #Returns an average euclidian distance for all the points on the 5 closest faces
            return op1, op2, op3, op4

        except (FileNotFoundError, AttributeError, IndexError, NameError, ValueError): #Error handling when there's errors in the csv
            print("Error: Incorrect CSV name, the adults specified do not exist, or their data is corrupted.")
            return None, None, None, None, None #Return empty lists

#Retrieves selected adult from the csvfile. 
def get_adult(filename, substring):

    with open(filename) as f: #gets file length and saves to stop the search for a name that doesnt exist
        file_length = sum(1 for line in f)

    file_read = open(filename, 'r') #read the file
    getline = file_read.readline()
    adult = []
    index = 0
    while getline: #Iterates through entire document until 15 matches found, or if there arent enough rows 
        if substring in getline and len(adult) <= 15: #stop after 15 tries
            adult.append(getline)
            index += 1
            getline = file_read.readline()
        elif len(adult) <= 15:
            index += 1
            getline = file_read.readline()
        elif ((index == file_length) and (len(adult) == 0)): #If the file is read through and the adult doesn't exist
            raise ValueError('The specified adult does not exist.')

    file_read.close()
    return adult #returns list with each index containing a row, and the headers column as a list to swap columns if needed

#Take an adults values (as a 2d list) and perform a euclidian analysis. 
def euc_analysis(list_in_2d):
    #Create a dictionary to hold the values from euclidian calculations
    facial_distances = {'FW': float, 'OCW': float, 'LEFL': float, 'REFL': float, 'ICW': float, 'NW': float, 'ABW': float, 'MW': float, 'NBL': float, 'NH': float}
    #Each index stores the two required rows and what facial feature they will create once calculated
    list_of_required_distances = [["FT_L", "FT_R", "FW"], ["EX_L", "EX_R", "OCW"], ["EX_L", "EN_L", "LEFL"], ["EN_R", "EX_R", "REFL"], \
        ["EN_L", "EN_R", "ICW"], ["AL_L", "AL_R", "NW"], ["SBAL_L", "SBAL_R", "ABW"], ["CH_L", "CH_R", "MW"], ["N", "PRN", "NBL"], ["N", "SN", "NH"]]

    analysed_features = 0 #How many facial distances have been caculated
    equation_rows = [[],[]] #2d list to hold both desired equations
    #Iterate through the 2d adult array and perform calculations
    while analysed_features < 10:
        distance_to_calculate = list_of_required_distances[analysed_features][2] #Get the name of what facial distance the calculation will create
        req_value_1, req_value_2 = list_of_required_distances[analysed_features][0], list_of_required_distances[analysed_features][1] #Get the two required rows to create the calculation

        values_found = 0 #How many rows for the calculation have been found
        search_2d_adult = 0 #Set back to 0 to search through all input array values again
        for search_2d_adult in range(15): 

            curr_adult_row = list_in_2d[search_2d_adult]  #Curr row of the adult being tested for calculation match
            #When a row found matches the x1,y1,z1
            if req_value_1 == curr_adult_row[1]:
                equation_rows[0] = curr_adult_row #Sets the first equation
                values_found += 1

            #When a row found matches the x2,y2,z2
            if req_value_2 == curr_adult_row[1]:
                equation_rows[1] = curr_adult_row #Sets the first equation
                values_found += 1
                
            if (values_found == 2): #once both values are matched, create the xyz values
                x1, y1, z1 = equation_rows[0][2], equation_rows[0][3], equation_rows[0][4]
                x2, y2, z2 = equation_rows[1][2], equation_rows[1][3], equation_rows[1][4]
                facial_distances[distance_to_calculate] = euc_analysis_formula(x1, y1, z1, x2, y2, z2) #Apply the euclidian formula to the xyz values
                analysed_features += 1
                break
    return facial_distances

#do the EUC analysus
def euc_analysis_formula(x1, y1, z1, x2, y2, z2):
    euc_formula_output = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5
    return euc_formula_output

#Perform cosine analysis
def cos_similarity(adult_1_euc, adult_2_euc):

    #Take only the float values and convert it to a list
    adult_1_list = list(adult_1_euc.values())
    adult_2_list = list(adult_2_euc.values())

    #Create numerator (values to be divided), and the A + B values for the denominator
    equation_numerator = 0
    equation_denominator_a = 0
    equation_denominator_b = 0

    for curr_index in range(10):    #EQ_numerator = sum of all A*B values, EQ_denomA/B = Sqrt(sum of all A^2) * Sqrt(sum of all B^2)
        equation_numerator += (adult_1_list[curr_index] * adult_2_list[curr_index])
        equation_denominator_a += (adult_1_list[curr_index]**2)
        equation_denominator_b += (adult_2_list[curr_index]**2)
    cosine_similarity = ( equation_numerator / ((equation_denominator_a**0.5) * (equation_denominator_b**0.5)) )

    return cosine_similarity

#Create 2d array with all the input file values
def get_all_adults(csv, adult_1, adult_2):

    #Get csv file length so the loop knows when to stop
    with open(csv) as f:
        file_length = sum(1 for line in f)
    
    #Initialise empty 2d list
    all_values = [[0] * 5 for i in range(file_length)]

    #Go through file line by line, check values and insert to the new list
    file_read = open(csv, 'r')
    getline = ((file_read.readline()).replace('\n', '')).split(',') #reads the first line (headers row)
    getline = ((file_read.readline()).replace('\n', '')).split(',') #skips to next line
    curr_line = 0
    while curr_line < file_length: #do for every line of the file
        if len(getline) > 1: #checks if line isnt empty
            all_values[curr_line][0] = getline[0] #and adds each line to the 2d list
            all_values[curr_line][1] = getline[1]
            all_values[curr_line][2] = getline[2]
            all_values[curr_line][3] = getline[3]
            all_values[curr_line][4] = getline[4]
            if curr_line > 0: #Avoid the header row
                for index in range(4):
                    check_bounds = all_values[curr_line][index]
                    if (check_bounds).isnumeric() == True: #Makes sure the XYZ values are between the |200| range, and makes the rows invalid if not
                        if (-200 > check_bounds > 200): #When the data is out of bounds, make the whole line invalid (doesnt get rid of name though)
                            all_values[curr_line][0], all_values[curr_line][1], all_values[curr_line][2], all_values[curr_line][3], all_values[curr_line][4] = None, None, None, None, None
            curr_line += 1
            getline = ((file_read.readline()).replace('\n', '')).split(',') #gets the next line
        else:
            curr_line += 1
            getline = ((file_read.readline()).replace('\n', '')).split(',')
    file_read.close()

    return analyse_whole_file(all_values, adult_1, adult_2) #Starts recusrive return values, which is chained to the return value of the next function

#Create euc distance measurements for face 1 to all faces, then face 2 to all faces. 
def analyse_whole_file(adults_in_2d, adult_1, adult_2):
    adults_start = 0
    adults_finish = 15
    adult_1_euc, adult_2_euc = euc_analysis(adult_1), euc_analysis(adult_2) #retrieve eucs again for the adults first input

    adults_compared_to_A1 = [[0] * 2 for i in range((len(adults_in_2d) // 15))] #create 2d list to hold the adult ID and cosine value for adult1
    adults_compared_to_A2 = [[0] * 2 for i in range((len(adults_in_2d) // 15))] #create 2d list to hold the adult ID and cosine value for adult2
    
    for current_adult_analysed in range((len(adults_in_2d) - 1)):

        current_adult2d = adults_in_2d[adults_start:adults_finish] #get the 15 rows of the adult thing

        if current_adult2d[0][0] != 0:

            for index in range(15):
                current_adult2d[index][2], current_adult2d[index][3], current_adult2d[index][4] = \
                    float(current_adult2d[index][2]), float(current_adult2d[index][3]), float(current_adult2d[index][4])
                current_adult2d[index][0], current_adult2d[index][1] = current_adult2d[index][0].upper(), current_adult2d[index][1].upper()

            #create euc analysis
            current_adult_euc = euc_analysis(current_adult2d)
            
            adults_compared_to_A1[current_adult_analysed][0] = current_adult2d[0][0] #Add the compared adult to the adults_compared list
            adults_compared_to_A1[current_adult_analysed][1] = cos_similarity(adult_1_euc, current_adult_euc) #get cosine
            adults_compared_to_A2[current_adult_analysed][0] = current_adult2d[0][0]
            adults_compared_to_A2[current_adult_analysed][1] = cos_similarity(adult_2_euc, current_adult_euc)
            
            adults_start += 15 #add 15 to to go the next adult profile
            adults_finish += 15

    return find_top5_closest(adults_compared_to_A1, adults_compared_to_A2) #returns the value of the top 5 adults which is a single list containing tuples

#Sifts through the list and matches the 5 most similar tuples
def find_top5_closest(adults_compared_to_A1, adults_compared_to_A2):

    adults_compared_to_A1.sort(key=lambda row: (row[1], row[0]), reverse=True) #Sorts the list numerically, then alphabetically if the numbers are the same
    adults_compared_to_A2.sort(key=lambda row: (row[1], row[0]), reverse=True)
    
    if adults_compared_to_A1[0][1] == 1.0: #If the value is 1 its the same adult, so delete that value
        del adults_compared_to_A1[0]
    if adults_compared_to_A2[0][1] == 1.0:
        del adults_compared_to_A2[0]    

    top_5_adultsA1 = adults_compared_to_A1[0:6] #gets the top 5 of each adult match
    top_5_adultsA2 = adults_compared_to_A2[0:6]
    list_of_tuples = [[0] * 5 for i in range(2)] #Initialise the list which will hold the tuples 

    for index in range(5): #Rounds the values, then creates a tuple and appends the tuple to the list containing them
        
        top_5_adultsA1[index][1] = round(top_5_adultsA1[index][1], 4)
        top_5_adultsA2[index][1] = round(top_5_adultsA2[index][1], 4)

        if top_5_adultsA1[index][1] == top_5_adultsA1[index + 1][1]: #Extra step in case the sort method did not properly sort alphabetically
            string1 = top_5_adultsA1[index][0]
            string2 = top_5_adultsA1[index + 1][0]
            if string1[0] > string2[0]:
                top_5_adultsA1[index], top_5_adultsA1[index + 1] = top_5_adultsA1[index + 1], top_5_adultsA1[index]
        if top_5_adultsA2[index][1] == top_5_adultsA2[index + 1][1]:
            string1 = top_5_adultsA2[index][0]
            string2 = top_5_adultsA2[index + 1][0]
            if string1[0] > string2[0]:
                top_5_adultsA2[index], top_5_adultsA2[index + 1] = top_5_adultsA2[index + 1], top_5_adultsA2[index]
        
        list_of_tuples[0][index] = tuple(top_5_adultsA1[index]) #Adds the tuple to the list
        list_of_tuples[1][index] = tuple(top_5_adultsA2[index])

    return list_of_tuples

#op4, use the closest 5 adults of each input to crate an average of each 10 facial distances
def avg_facial_distances(tuples_list, csv):

    closest_adults_1 = [] #create two empty lists
    closest_adults_2 = []
    #Create an averages dictionary for each face
    averages_a1 = {'FW': float, 'OCW': float, 'LEFL': float, 'REFL': float, 'ICW': float, 'NW': float, 'ABW': float, 'MW': float, 'NBL': float, 'NH': float}
    averages_a2 = {'FW': float, 'OCW': float, 'LEFL': float, 'REFL': float, 'ICW': float, 'NW': float, 'ABW': float, 'MW': float, 'NBL': float, 'NH': float}
    averages_keys = ["FW", "OCW", "LEFL", "REFL", "ICW", "NW", "ABW", "MW", "NBL", "NH"] #keys for altering the dictionary

    for index in range(5): #Manually searches file for each of the 5 adults, and runs the functions to get the euclidian distance values
        closest_adults_1.append(list((euc_analysis(make_2d(get_adult(csv, tuples_list[0][index][0])))).values()))
        closest_adults_2.append(list((euc_analysis(make_2d(get_adult(csv, tuples_list[1][index][0])))).values()))

    for index in range(10): #Loop through all 10 dictionary values for both 5 closest adults to find average
        index_average_a1 = 0
        index_average_a2 = 0
        current_dict_key = averages_keys[index] #Use this to know which dictionary key to use
        for sub_index in range(5): #Averages each 5 adults key values
            index_average_a1 += closest_adults_1[sub_index][index]
            index_average_a2 += closest_adults_2[sub_index][index]
        averages_a1[current_dict_key] = (round(index_average_a1 / 5, 4)) #appends to list and rounds
        averages_a2[current_dict_key] = (round(index_average_a2 / 5, 4))

    return averages_a1, averages_a2

def make_2d(list):
    list_in_2d = [[0] * 5 for i in range(15)] #initialise 2d list (3x, 10y)
    input_list_index = 0                      #index counter for input array
    while input_list_index < len(list): 
        new_2D_index, facial_point_index = 0, 0 
        facial_point_iteration = list[input_list_index]            #create instance variable to a single facial points x,y,z values
        facial_point_iteration = facial_point_iteration.replace('\n', '')
        facial_point_iteration = facial_point_iteration.split(',') #remove carriage return and split using commas
        while new_2D_index < 5: #Iterate through by adding each rows point number & XYZ values first
            list_in_2d[input_list_index][new_2D_index] = facial_point_iteration[facial_point_index]
            new_2D_index += 1
            facial_point_index += 1
        input_list_index += 1
    for index in range(15): #Cast all XYZ values to floats, and turn characters into uppercase
        list_in_2d[index][2], list_in_2d[index][3], list_in_2d[index][4] = \
            float(list_in_2d[index][2]), float(list_in_2d[index][3]), float(list_in_2d[index][4])
        list_in_2d[index][0], list_in_2d[index][1] = list_in_2d[index][0].upper(), list_in_2d[index][1].upper()
    return list_in_2d #Returns 2D list, with sub indexes referring to each facial point and their XYZ values

# Take a dictionary and round all its values
def dict_rounder(dict_to_round):
#iterates through each key and value
    for key, value in dict_to_round.items(): 
        dict_to_round[key] = round(value, 4) #parses it into argument
    return dict_to_round