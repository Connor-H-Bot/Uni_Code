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
    return True #return value to stop printing    

# Calibrate data and perform asymmetry analysis
def asymmetry_analysis(list_in_2d):
    float_list = [[float(element) for element in list_inner] for list_inner in list_in_2d] #convert all numbers to floats
    if (float_list[9][0] and float_list[9][1] and float_list[9][2]) == 0: #if nose is already 0 do not calibrate
        return float_list

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