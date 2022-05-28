def main(csv, adults_array):
    #TODO add checks for if csv exists and two valid inputs to array
    op3 = get_all_adults(csv)
    adult_1 = make_2d(get_adult(op3, adults_array[0]))
    adult_2 = make_2d(get_adult(csv, adults_array[1]))
    adult_1_euc = euc_analysis(adult_1)
    adult_2_euc = euc_analysis(adult_2)
    op1 = (adult_1_euc, adult_2_euc) #TODO round values on the way out
    op2 = round(cos_similarity(adult_1_euc, adult_2_euc), 4)
    return op1



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
        value_found_bool = False #Whether the two values have been found (use to break the loop below)

        search_2d_adult = 0 #Set back to 0 to search through all input array values again
        for search_2d_adult in range(15): 

            #Break this for loop once calculation complete
            if value_found_bool == True:
                break

            curr_adult_row = list_in_2d[search_2d_adult]  #Curr row of the adult being tested for calculation match

            #When a row found matches the x1,y1,z1
            if req_value_1 == curr_adult_row[0]:
                equation_rows[0] = curr_adult_row #Sets the first equation
                values_found += 1

            #When a row found matches the x2,y2,z2
            if req_value_2 == curr_adult_row[0]:
                equation_rows[1] = curr_adult_row #Sets the first equation
                values_found += 1
                
            if (values_found == 2):
                x1, y1, z1 = equation_rows[0][1], equation_rows[0][2], equation_rows[0][3]
                x2, y2, z2 = equation_rows[1][1], equation_rows[1][2], equation_rows[1][3]
                facial_distances[distance_to_calculate] = euc_analysis_formula(x1, y1, z1, x2, y2, z2)
                value_found_bool = True
                analysed_features += 1
    
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
    #EQ_numerator = sum of all A*B values, EQ_denomA/B = Sqrt(sum of all A^2) * Sqrt(sum of all B^2)
    for curr_index in range(10):
        equation_numerator += (adult_1_list[curr_index] * adult_2_list[curr_index])
        equation_denominator_a += (adult_1_list[curr_index]**2)
        equation_denominator_b += (adult_2_list[curr_index]**2)
    cosine_similarity = ( equation_numerator / ((equation_denominator_a**0.5) * (equation_denominator_b**0.5)) )

    return cosine_similarity



#Create 2d array with all the input file values
def get_all_adults(csv):

    #Get csv file length so the loop knows when to stop
    with open(csv) as f:
        file_length = sum(1 for line in f)
    
    #Initialise empty 2d list
    all_values = [[0] * 5 for i in range(file_length)]

    #Go through file line by line, check values and insert to the new list
    file_read = open(csv, 'r')
    getline = ((file_read.readline()).replace('\n', '')).split(',')
    curr_line = 0
    while curr_line < file_length:
        all_values[curr_line][0] = getline[0]
        all_values[curr_line][1] = getline[1]
        all_values[curr_line][2] = getline[2]
        all_values[curr_line][3] = getline[3]
        all_values[curr_line][4] = getline[4]
        if curr_line > 0:
            for index in range(4):
                check_bounds = all_values[curr_line][index]
                if (check_bounds).isnumeric() == True:
                    if (-200 > check_bounds > 200):
                        all_values[curr_line][0], all_values[curr_line][1], all_values[curr_line][2], all_values[curr_line][3], all_values[curr_line][4] = None, None, None, None, None
        curr_line += 1
        getline = ((file_read.readline()).replace('\n', '')).split(',')

    file_read.close()
    return all_values


#Retrieves selected adult from the csvfile. 
#Reads line by line, so it works if theres gaps between required rows
def get_adult(filename, substring):
    file_read = open(filename, 'r')
    getline = file_read.readline()
    adult = []
    while getline: #Iterates through ire docum until 
        if substring in getline and len(adult) <= 15: #stop after 15 ries
            adult.append(getline)
            getline = file_read.readline()
        elif len(adult) <= 15:
            getline = file_read.readline()
    file_read.close()
    return adult #returns list with each index containing a row

#Get adult by searching through created list containing all values
def get_adult(list, adult):
    adult = []
    return False



def make_2d(list):
    list_in_2d = [[0] * 4 for i in range(15)] #initialise 2d list (3x, 10y)
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
    for index in range(15): #Cast all XYZ values to floats, and turn characters into uppercase
        list_in_2d[index][1], list_in_2d[index][2], list_in_2d[index][3] = float(list_in_2d[index][1]), float(list_in_2d[index][2]), float(list_in_2d[index][3])
        list_in_2d[index][0] = list_in_2d[index][0].upper()
    return list_in_2d #Returns 2D list, with sub indexes referring to each facial point and their XYZ values



# Take a 1d list as input and round all elems to 4 decimal places
def list_rounder(list_to_round):
    list_rounded = []
    for index in range(len(list_to_round)): 
        list_rounded.append(round(list_to_round[index], 4)) #Does not change order
        index += 1
    return list_rounded 



print(main('sample_face_data.csv', ['R7033', 'P1283']))