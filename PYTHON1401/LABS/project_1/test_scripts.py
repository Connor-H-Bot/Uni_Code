def read_file(filename):
    file_interior = open(filename, 'r')
    data = file_interior.read()
    file_interior.close()
    print(data)

# Get adult based on ID
def get_adult(filename, substring):
    file_read = open(filename, 'r')
    getline = file_read.readline()
    adult = []
    while getline:
        if substring in getline:
            adult.append(getline)
            getline = file_read.readline()
        else:
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
    return True #return true to avoid printing whole thing   

# Calibrate data and perform asymmetry analysis
def asymmetry_analysis(list_in_2d):
    float_list = [[float(element) for element in list_inner] for list_inner in list_in_2d] #convert all numbers to floats
    asymmetry_analysis_list = [] #Store values for each facial points analysis
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

# Return 2x values, lowest asymmetry values for upper and lower face
def get_min_asymmetry(asymmetry_analysis_list):
    min_asymmetry = []  
    for index in range(len(asymmetry_analysis_list)):
        current_number = asymmetry_analysis_list[index]
        if index < 5:
            if current_number > asymmetry_analysis_list[index + 1]:
                min_asymmetry[0] = current_number
        if index > 5:
            if current_number > asymmetry_analysis_list[index + 1]:
                min_asymmetry[1] = current_number
    return min_asymmetry  

# Return 2x values, lowest asymmetry values for upper and lower face
def get_max_asymmetry(asymmetry_analysis_list):
    max_asymmetry = [] 
    return

# Return 2x values, lowest asymmetry values for upper and lower face
def get_avg_asymmetry(asymmetry_analysis_list):
    avg_asymmetry = []  
    return

# Return 2x values, lowest asymmetry values for upper and lower face
def get_stddev_asymmetry(asymmetry_analysis_list):
    stddev_asymmetry = [] 
    return

print(get_min_asymmetry([3.1383725030943417, 3.8951716918507517, 4.083771247610689, 3.2533008074832215, 1.2949654758688547, 3.1759220224928937, 2.7899458412031803, 3.319477928377509, 2.7003713645071215]))

print(asymmetry_analysis([['-0.98523866', '0.758461395', '-0.74612129'], \
    ['0.90410184', '0.713141558', '-0.716118938'], \
        ['-0.907987111', '-0.711881409', '-0.716405858'], \
            ['-0.908010738', '0', '-0.717976775'], \
                ['-0.90402733', '-0.713459067', '0.720054384'], \
                    ['-0.897653614', '-0.716625797', '-0.722117174'], \
                        ['0.878833765', '0.72272582', '0.725302538'], \
                            ['-0.867293118', '-0.723656965', '-0.724962529'], \
                                ['-0.851736792', '0.724907156', '-0.720590106'], \
                                    ['0', '0', '0']]))

#print(get_adult('asymmetry_sample.csv', 'J7033'))
print(make_2d(['J7033,1,-0.98523866,0.758461395,-0.74612129\n', \
    'J7033,2,0.90410184,0.713141558,-0.716118938\n', \
        'J7033,3,-0.907987111,-0.711881409,-0.716405858\n', \
            'J7033,4,-0.908010738,0,-0.717976775\n', \
                'J7033,5,-0.90402733,-0.713459067,0.720054384\n', \
                    'J7033,6,-0.897653614,-0.716625797,-0.722117174\n', \
                        'J7033,7,0.878833765,0.72272582,0.725302538\n', \
                            'J7033,8,-0.867293118,-0.723656965,-0.724962529\n', \
                                'J7033,9,-0.851736792,0.724907156,-0.720590106\n', \
                                    'J7033,10,0,0,0\n']))
